import { defineVitestConfig } from '@nuxt/test-utils/config';
export default defineVitestConfig({
  test: {
    environment: 'nuxt',
    globals: true,
    environmentOptions: {
      nuxt: {}
    },
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'json'],
      reportsDirectory: './tests/unit/coverage',
      thresholds: {
        statements: 95,
        branches: 95
      },
      exclude: [
        '**/*.config.ts',
        '**/*.config.mjs',
        '**/.nuxt/**',
        'types/**',
        'api/index.ts',
        'composables/useAPI.ts',
        'api/clients/**'
      ]
    }
  }
});
