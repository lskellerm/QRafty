module.exports = {
  root: true,
  extends: [
    "@nuxt/eslint-config",
    "@nuxt/eslint-config",
    "@nuxtjs/eslint-config-typescript",
    "plugin:prettier/recommended"
  ],

  rules: {
    semi: ["error", "always"],
    "no-console": "off"
  }
};
