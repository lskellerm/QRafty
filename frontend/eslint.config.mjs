// @ts-check
import withNuxt from './.nuxt/eslint.config.mjs';
import prettier from 'eslint-plugin-prettier';
import eslintPluginPrettierRecommended from 'eslint-plugin-prettier/recommended';

export default withNuxt(
  // Your custom configs here
  {
    files: ['**/*.js', '**/*.vue', '**/*.ts'],
    ignores: ['.gitignore'],
    rules: {
      'no-console': 'off',
      semi: ['error', 'always']
    },
    plugins: {
      prettier
    }
  },
  eslintPluginPrettierRecommended
);
