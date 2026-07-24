#!/usr/bin/env node

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import process from "node:process";
import { parseArgs } from "node:util";
import {
  GENERATED_SKILLS_ROOT,
  loadCatalogue,
  skillDirectories,
  skillsForBundles,
  validateBundles,
} from "./opencode-bundle-lib.mjs";

const MANIFEST_NAME = ".skillery-manifest.json";

function usage() {
  return `Usage:
  skillery-opencode list
  skillery-opencode install <bundle> [<bundle> ...] [--global | --project | --target <dir>] [--force] [--dry-run]
  skillery-opencode uninstall <bundle> [<bundle> ...] [--global | --project | --target <dir>] [--dry-run]
  skillery-opencode status [--global | --project | --target <dir>]

Targets:
  --global       ~/.config/opencode/skills (default)
  --project      <cwd>/.opencode/skills
  --target DIR   Explicit skills directory

Examples:
  skillery-opencode install meaningfy-core --global
  skillery-opencode install meaningfy-core meaningfy-building --project
  skillery-opencode uninstall meaningfy-core --global
`;
}

function parseCli(argv) {
  const parsed = parseArgs({
    args: argv,
    allowPositionals: true,
    strict: true,
    options: {
      global: { type: "boolean", default: false },
      project: { type: "boolean", default: false },
      target: { type: "string" },
      force: { type: "boolean", default: false },
      "dry-run": { type: "boolean", default: false },
      help: { type: "boolean", short: "h", default: false },
      version: { type: "boolean", short: "v", default: false },
    },
  });

  const [command, ...bundles] = parsed.positionals;
  return { command, bundles, ...parsed.values, dryRun: parsed.values["dry-run"] };
}

function targetRoot(options) {
  const selected = [options.global, options.project, Boolean(options.target)].filter(Boolean).length;
  if (selected > 1) throw new Error("Choose only one of --global, --project, or --target");
  if (options.target) return path.resolve(options.target);
  if (options.project) return path.join(process.cwd(), ".opencode", "skills");
  return path.join(os.homedir(), ".config", "opencode", "skills");
}

function manifestPath(target) {
  return path.join(target, MANIFEST_NAME);
}

function emptyInstallManifest(catalogue) {
  return {
    schemaVersion: 1,
    catalogueVersion: catalogue.version,
    source: "meaningfy-ws/skillery",
    installedBundles: {},
    managedSkills: [],
  };
}

function readInstallManifest(target, catalogue) {
  const filename = manifestPath(target);
  if (!fs.existsSync(filename)) return emptyInstallManifest(catalogue);
  let parsed;
  try {
    parsed = JSON.parse(fs.readFileSync(filename, "utf8"));
  } catch (error) {
    throw new Error(`Cannot read ${filename}: ${error.message}`);
  }
  if (parsed.schemaVersion !== 1 || !parsed.installedBundles || !Array.isArray(parsed.managedSkills)) {
    throw new Error(`Unsupported or invalid Skillery installation manifest: ${filename}`);
  }
  return parsed;
}

function writeJsonAtomic(filename, value) {
  fs.mkdirSync(path.dirname(filename), { recursive: true });
  const temporary = `${filename}.tmp-${process.pid}`;
  fs.writeFileSync(temporary, `${JSON.stringify(value, null, 2)}\n`, "utf8");
  try {
    fs.renameSync(temporary, filename);
  } catch (error) {
    if (!fs.existsSync(filename)) throw error;
    fs.rmSync(filename, { force: true });
    fs.renameSync(temporary, filename);
  }
}

function copyDirectoryAtomic(source, destination) {
  const parent = path.dirname(destination);
  fs.mkdirSync(parent, { recursive: true });
  const temporary = path.join(parent, `.skillery-${path.basename(destination)}-${process.pid}-${Date.now()}`);
  fs.rmSync(temporary, { recursive: true, force: true });
  fs.cpSync(source, temporary, { recursive: true, force: true });
  fs.rmSync(destination, { recursive: true, force: true });
  fs.renameSync(temporary, destination);
}

function recomputeManagedSkills(catalogue, installedBundles) {
  const names = Object.keys(installedBundles).filter((name) => Object.hasOwn(catalogue.bundles, name));
  return skillsForBundles(catalogue, names);
}

function commandList(catalogue) {
  for (const bundle of Object.keys(catalogue.bundles).sort()) {
    console.log(`${bundle} (${catalogue.bundles[bundle].length})`);
    for (const skill of catalogue.bundles[bundle]) console.log(`  - ${skill}`);
  }
}

function commandStatus(catalogue, options) {
  const target = targetRoot(options);
  const manifest = readInstallManifest(target, catalogue);
  console.log(`Target: ${target}`);
  console.log(`Catalogue: ${catalogue.version}`);
  const bundles = Object.keys(manifest.installedBundles).sort();
  if (bundles.length === 0) {
    console.log("Installed bundles: none");
    return;
  }
  console.log("Installed bundles:");
  for (const bundle of bundles) {
    const installed = manifest.installedBundles[bundle];
    console.log(`  - ${bundle} (${installed.catalogueVersion})`);
  }
}

function commandInstall(catalogue, requested, options) {
  const bundles = validateBundles(catalogue, requested);
  if (bundles.length === 0) throw new Error("Specify at least one bundle to install");
  const target = targetRoot(options);
  const manifest = readInstallManifest(target, catalogue);
  const currentlyManaged = new Set(manifest.managedSkills);
  const skills = skillDirectories(catalogue, bundles, GENERATED_SKILLS_ROOT);

  for (const skill of skills) {
    const destination = path.join(target, skill.name);
    if (fs.existsSync(destination) && !currentlyManaged.has(skill.name) && !options.force) {
      throw new Error(
        `Refusing to overwrite unmanaged skill '${skill.name}' at ${destination}. ` +
          "Move it, remove it, or rerun with --force.",
      );
    }
  }

  console.log(`${options.dryRun ? "Would install" : "Installing"} ${bundles.join(", ")} into ${target}`);
  for (const skill of skills) {
    const destination = path.join(target, skill.name);
    console.log(`  ${options.dryRun ? "would copy" : "copy"} ${skill.name}`);
    if (!options.dryRun) copyDirectoryAtomic(skill.directory, destination);
  }

  if (options.dryRun) return;
  for (const bundle of bundles) {
    manifest.installedBundles[bundle] = {
      catalogueVersion: catalogue.version,
      skills: [...catalogue.bundles[bundle]],
    };
  }
  manifest.catalogueVersion = catalogue.version;
  manifest.managedSkills = recomputeManagedSkills(catalogue, manifest.installedBundles);
  writeJsonAtomic(manifestPath(target), manifest);
  console.log("Restart OpenCode so it refreshes skill discovery.");
}

function commandUninstall(catalogue, requested, options) {
  const bundles = validateBundles(catalogue, requested);
  if (bundles.length === 0) throw new Error("Specify at least one bundle to uninstall");
  const target = targetRoot(options);
  const manifest = readInstallManifest(target, catalogue);
  const previouslyManaged = new Set(manifest.managedSkills);
  for (const bundle of bundles) delete manifest.installedBundles[bundle];
  const stillManaged = new Set(recomputeManagedSkills(catalogue, manifest.installedBundles));
  const removable = [...previouslyManaged].filter((skill) => !stillManaged.has(skill)).sort();

  console.log(`${options.dryRun ? "Would uninstall" : "Uninstalling"} ${bundles.join(", ")} from ${target}`);
  for (const skill of removable) {
    const destination = path.join(target, skill);
    console.log(`  ${options.dryRun ? "would remove" : "remove"} ${skill}`);
    if (!options.dryRun) fs.rmSync(destination, { recursive: true, force: true });
  }

  if (options.dryRun) return;
  manifest.catalogueVersion = catalogue.version;
  manifest.managedSkills = [...stillManaged];
  if (Object.keys(manifest.installedBundles).length === 0) {
    fs.rmSync(manifestPath(target), { force: true });
  } else {
    writeJsonAtomic(manifestPath(target), manifest);
  }
  console.log("Restart OpenCode so it refreshes skill discovery.");
}

function main() {
  const options = parseCli(process.argv.slice(2));
  const catalogue = loadCatalogue();

  if (options.version) {
    console.log(catalogue.version);
    return;
  }
  if (options.help || !options.command) {
    console.log(usage());
    return;
  }

  switch (options.command) {
    case "list":
      commandList(catalogue);
      return;
    case "status":
      commandStatus(catalogue, options);
      return;
    case "install":
      commandInstall(catalogue, options.bundles, options);
      return;
    case "uninstall":
      commandUninstall(catalogue, options.bundles, options);
      return;
    default:
      throw new Error(`Unknown command '${options.command}'\n\n${usage()}`);
  }
}

try {
  main();
} catch (error) {
  console.error(`skillery-opencode: ${error.message}`);
  process.exitCode = 1;
}
