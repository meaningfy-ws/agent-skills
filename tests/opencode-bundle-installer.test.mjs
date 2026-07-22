import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { fileURLToPath } from "node:url";

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const CLI = path.join(REPO, "tools", "skillery-opencode.mjs");

function fixture() {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "skillery-test-"));
  fs.mkdirSync(path.join(root, ".opencode", "skills", "alpha"), { recursive: true });
  fs.mkdirSync(path.join(root, ".opencode", "skills", "beta"), { recursive: true });
  fs.writeFileSync(
    path.join(root, ".opencode", "bundles.json"),
    JSON.stringify({ version: "9.9.9", bundles: { "meaningfy-core": ["alpha", "beta"] } }),
  );
  fs.writeFileSync(path.join(root, ".opencode", "skills", "alpha", "SKILL.md"), "---\nname: alpha\ndescription: A\n---\n");
  fs.writeFileSync(path.join(root, ".opencode", "skills", "beta", "SKILL.md"), "---\nname: beta\ndescription: B\n---\n");
  return root;
}

function run(root, ...args) {
  return spawnSync(process.execPath, [CLI, ...args], {
    encoding: "utf8",
    env: { ...process.env, SKILLERY_REPOSITORY_ROOT: root },
  });
}

test("installs and uninstalls one bundle", () => {
  const root = fixture();
  const target = path.join(root, "target");

  const installed = run(root, "install", "meaningfy-core", "--target", target);
  assert.equal(installed.status, 0, installed.stderr);
  assert.ok(fs.existsSync(path.join(target, "alpha", "SKILL.md")));
  assert.ok(fs.existsSync(path.join(target, "beta", "SKILL.md")));
  const manifest = JSON.parse(fs.readFileSync(path.join(target, ".skillery-manifest.json"), "utf8"));
  assert.deepEqual(manifest.managedSkills, ["alpha", "beta"]);

  const uninstalled = run(root, "uninstall", "meaningfy-core", "--target", target);
  assert.equal(uninstalled.status, 0, uninstalled.stderr);
  assert.equal(fs.existsSync(path.join(target, "alpha")), false);
  assert.equal(fs.existsSync(path.join(target, ".skillery-manifest.json")), false);
});

test("refuses to overwrite an unmanaged skill", () => {
  const root = fixture();
  const target = path.join(root, "target");
  fs.mkdirSync(path.join(target, "alpha"), { recursive: true });
  fs.writeFileSync(path.join(target, "alpha", "SKILL.md"), "local\n");

  const result = run(root, "install", "meaningfy-core", "--target", target);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Refusing to overwrite unmanaged skill 'alpha'/);
  assert.equal(fs.readFileSync(path.join(target, "alpha", "SKILL.md"), "utf8"), "local\n");
});

test("rejects an unknown bundle", () => {
  const root = fixture();
  const result = run(root, "install", "not-a-bundle", "--target", path.join(root, "target"));
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Unknown Skillery bundle/);
});

test("plugin infers a bundle from the git dependency alias", () => {
  const parent = fs.mkdtempSync(path.join(os.tmpdir(), "skillery-plugin-test-"));
  const root = path.join(parent, "meaningfy-core");
  fs.mkdirSync(path.join(root, ".opencode", "skills", "alpha"), { recursive: true });
  fs.writeFileSync(
    path.join(root, ".opencode", "bundles.json"),
    JSON.stringify({
      version: "9.9.9",
      bundles: { "meaningfy-core": ["alpha"], "meaningfy-building": ["beta"] },
    }),
  );
  fs.writeFileSync(path.join(root, ".opencode", "skills", "alpha", "SKILL.md"), "---\nname: alpha\ndescription: A\n---\n");

  const plugin = path.join(REPO, "tools", "opencode-plugin.mjs");
  const script = `
    const { default: load } = await import(${JSON.stringify(`file://${plugin}`)});
    const hooks = await load({}, {});
    const config = {};
    await hooks.config(config);
    process.stdout.write(JSON.stringify(config));
  `;
  const result = spawnSync(process.execPath, ["--input-type=module", "-e", script], {
    encoding: "utf8",
    env: { ...process.env, SKILLERY_REPOSITORY_ROOT: root },
  });
  assert.equal(result.status, 0, result.stderr);
  const config = JSON.parse(result.stdout);
  assert.deepEqual(config.skills.paths, [path.join(root, ".opencode", "skills", "alpha")]);
});
