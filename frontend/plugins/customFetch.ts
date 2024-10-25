import type { $Fetch } from 'nitropack';
// Create a custom Nuxt Plugin to provide a custom $fetch instance.
export default defineNuxtPlugin(() => {
  // Extract base API url from the runtime config, determined by the environment
  const apiBaseUrl =
    /* v8 ignore next 4 */
    useRuntimeConfig().public.environment === 'testing'
      ? useRuntimeConfig().public.playwrightApiBaseUrl
      : useRuntimeConfig().public.apiBase;

  // Create a custom #fetch instance which wraps the default $fetch, adding options for to the custom QRafty API client
  const api: $Fetch = $fetch.create({
    baseURL: apiBaseUrl,
    onRequest: ({ request, options, error }) => {} // eslint-disable-line
  });
  return {
    provide: {
      api
    }
  };
});
