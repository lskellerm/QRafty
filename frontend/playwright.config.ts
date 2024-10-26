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
  // retries: process.env.CI ? 1 : 0,
  retries: 0,
  /* Limit the number of workers in CI environments, using default value in local */
  workers: process.env.CI ? 2 : undefined,
  reporter: [
    [
      'html',
      {
        outputFolder: 'tests/e2e/playwright-report',
        open: process.env.CI ? 'never' : 'always'
      }
    ]
  ],
  use: {
    baseURL: process.env.CI ? 'http://localhost:3000' : 'http://frontend:3000',
    headless: true,
    trace: 'retain-on-failure',
    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    nuxt: {
      /* Nuxt configuration options */
      rootDir: fileURLToPath(new URL('.', import.meta.url)),
      browser: false,
      host: process.env.CI ? 'http://localhost:3000' : 'http://frontend:3000'
    },
    // Use the ws endpoint for Playwright to connect to the browser when running locally to connect to the browser which is running in a docker container
    ...(process.env.CI
      ? {
          browserName: 'chromium'
        } // No wsEndpoint in CI, use default Chromium setup
      : {
          connectOptions: {
            wsEndpoint: 'ws://playwright:9222'
          }
        })
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
    url: process.env.CI ? 'http://localhost:3000' : 'http://frontend:3000',
    reuseExistingServer: !process.env.CI,
    stdout: 'pipe'
  }
});
