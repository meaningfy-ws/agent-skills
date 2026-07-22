import {
  inferBundleFromInstallAlias,
  loadCatalogue,
  normalizeBundleSelection,
  PACKAGE_ROOT,
  skillDirectories,
  validateBundles,
} from "./opencode-bundle-lib.mjs";

function selectedBundles(catalogue, options) {
  const configured = normalizeBundleSelection(options?.bundles ?? options?.bundle);
  if (configured.length > 0) return validateBundles(catalogue, configured);

  const fromEnvironment = normalizeBundleSelection(process.env.MEANINGFY_SKILLERY_BUNDLES);
  if (fromEnvironment.length > 0) return validateBundles(catalogue, fromEnvironment);

  const inferred = inferBundleFromInstallAlias(catalogue, PACKAGE_ROOT);
  if (inferred) return [inferred];

  return ["meaningfy-core"];
}

export default async function SkilleryOpenCodePlugin(_input, options = {}) {
  const catalogue = loadCatalogue();
  const bundles = selectedBundles(catalogue, options);
  const skills = skillDirectories(catalogue, bundles);

  return {
    config: async (config) => {
      config.skills ??= {};
      config.skills.paths ??= [];
      for (const skill of skills) {
        if (!config.skills.paths.includes(skill.directory)) {
          config.skills.paths.push(skill.directory);
        }
      }
    },
  };
}
