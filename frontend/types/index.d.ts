// Globally defined interfaces and types for the project
declare module '@nuxt/schema' {
  interface PublicRuntimeConfig {
    apiBase: string;
  }
}

declare module '#app' {
  import type { $Fetch } from 'nitropack';
  interface NuxtApp {
    $api: $Fetch;
  }
}

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $api: import('nitropack').$Fetch;
  }
}
export {};
