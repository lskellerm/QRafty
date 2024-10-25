import { defineConfig, devices } from '@playwright/test';
import { fileURLToPath } from 'node:url';
import type { ConfigOptions } from '@nuxt/test-utils/playwright';

const devicesToTest = ['Desktop Chrome'];

export default defineConfig<ConfigOptions>({
  testDir: './tests/e2e',
  outputDir: './tests/e2e/test-results',
  /* Run tests in files in parallel */
  fullyParallel: true,
  /* Fail the build in CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  /* Limit the number of workers in CI environments, using default value in local */
  workers: process.env.CI ? 2 : undefined,
  reporter: [
    [
      'html',
      {
        outputFolder: 'tests/e2e/test-results',
        open: process.env.CI ? 'never' : 'always'
      }
    ]
  ],
  use: {
    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    baseURL: 'http://frontend:3000',
    headless: true,
    trace: 'on-first-retry',
    nuxt: {
      /* Nuxt configuration options */
      rootDir: fileURLToPath(new URL('.', import.meta.url)),
      browser: false,
      host: 'http://frontend:3000'
    },
    connectOptions: {
      wsEndpoint: 'ws://playwright:9222'
    }
  },
  expect: {
    timeout: 20000
  },
  // Configure project for major browsers
  projects: devicesToTest.map((device) =>
    typeof device === 'string' ? { name: device, use: devices[device] } : device
  ),

  // Run a local dev server before starting the tests
  webServer: {
    command: 'pnpm dev',
    url: 'http://frontend:3000',
    reuseExistingServer: !process.env.CI
  }
});
