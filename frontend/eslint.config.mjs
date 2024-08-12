// @ts-check
import withNuxt from './.nuxt/eslint.config.mjs';
import js from '@eslint/js';
import prettier from 'eslint-config-prettier';
import eslintPluginPrettierRecommended from 'eslint-plugin-prettier/recommended';

export default withNuxt(
  // Your custom configs here
  {
    files: ['**/*.js', '**/*.vue', '**/*.ts'],
    ignores: [
      '.gitignore',
      'node_modules/',
      'dist/',
      '.nuxt/',
      '.pnpm-home/, .pnpm-lock.yaml'
    ],
    rules: {
      'no-console': 'off',
      semi: ['error', 'always']
    }
  },
  js.configs.recommended,
  prettier,
  eslintPluginPrettierRecommended
);
