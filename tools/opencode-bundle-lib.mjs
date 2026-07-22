import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const MODULE_DIR = path.dirname(fileURLToPath(import.meta.url));

export const PACKAGE_ROOT = path.resolve(
  process.env.SKILLERY_REPOSITORY_ROOT || path.join(MODULE_DIR, ".."),
);

export const BUNDLE_MANIFEST = path.join(PACKAGE_ROOT, ".opencode", "bundles.json");
export const GENERATED_SKILLS_ROOT = path.join(PACKAGE_ROOT, ".opencode", "skills");

export function loadCatalogue(manifestPath = BUNDLE_MANIFEST) {
  let parsed;
  try {
    parsed = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
  } catch (error) {
    throw new Error(`Cannot read Skillery bundle manifest at ${manifestPath}: ${error.message}`);
  }

  if (!parsed || typeof parsed !== "object" || typeof parsed.version !== "string") {
    throw new Error(`Invalid Skillery bundle manifest at ${manifestPath}: missing version`);
  }
  if (!parsed.bundles || typeof parsed.bundles !== "object" || Array.isArray(parsed.bundles)) {
    throw new Error(`Invalid Skillery bundle manifest at ${manifestPath}: missing bundles object`);
  }

  for (const [bundle, skills] of Object.entries(parsed.bundles)) {
    if (!Array.isArray(skills) || skills.some((skill) => typeof skill !== "string")) {
      throw new Error(`Invalid Skillery bundle '${bundle}': expected a list of skill names`);
    }
  }

  return parsed;
}

export function normalizeBundleSelection(value) {
  if (value === undefined || value === null) return [];
  const values = Array.isArray(value) ? value : [value];
  return values
    .flatMap((item) => String(item).split(","))
    .map((item) => item.trim())
    .filter(Boolean);
}

export function validateBundles(catalogue, requested) {
  const unique = [...new Set(normalizeBundleSelection(requested))];
  const unknown = unique.filter((name) => !Object.hasOwn(catalogue.bundles, name));
  if (unknown.length > 0) {
    const available = Object.keys(catalogue.bundles).sort().join(", ");
    throw new Error(`Unknown Skillery bundle(s): ${unknown.join(", ")}. Available: ${available}`);
  }
  return unique;
}

export function skillsForBundles(catalogue, bundles) {
  return [...new Set(bundles.flatMap((bundle) => catalogue.bundles[bundle]))].sort();
}

export function skillDirectories(catalogue, bundles, skillsRoot = GENERATED_SKILLS_ROOT) {
  return skillsForBundles(catalogue, bundles).map((skill) => {
    const directory = path.join(skillsRoot, skill);
    const definition = path.join(directory, "SKILL.md");
    if (!fs.existsSync(definition)) {
      throw new Error(`Bundle references missing generated skill: ${definition}`);
    }
    return { name: skill, directory };
  });
}

export function inferBundleFromInstallAlias(catalogue, packageRoot = PACKAGE_ROOT) {
  const alias = path.basename(packageRoot);
  return Object.hasOwn(catalogue.bundles, alias) ? alias : undefined;
}
