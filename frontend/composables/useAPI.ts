// Import types needed from Nuxt and NitroPack for type-checking
import type { UseFetchOptions } from 'nuxt/app';
import type { NitroFetchRequest, $Fetch } from 'nitropack';

// Define the custom composable function for making API calls to the QRafty API
export const useAPI: typeof useFetch = <T>(
  url: string | (() => string),
  options?: UseFetchOptions<T>
) => {
  return useFetch(url, {
    ...options,
    $fetch: useNuxtApp().$api as $Fetch<T, NitroFetchRequest>
  });
};
