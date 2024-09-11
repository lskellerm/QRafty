// https://nuxt.com/docs/api/configuration/nuxt-config
import { defineNuxtConfig } from 'nuxt/config';

export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  imports: {
    dirs: ['./api']
  },
  devtools: { enabled: true },
  typescript: {
    strict: true,
    typeCheck: true
  },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/eslint',
    'shadcn-nuxt',
    '@nuxt/image',
    '@nuxt/icon',
    '@formkit/auto-animate/nuxt',
    '@nuxt/test-utils/module'
  ],
  tailwindcss: {
    editorSupport: true
  },
  eslint: {},
  shadcn: {
    /**
     * Prefix for all the imported components
     */
    prefix: '',

    /**
     * Directory that the components live in
     * @default "./components/ui"
     */
    componentDir: './components/ui'
  },
  components: [
    {
      path: '~/components',
      pathPrefix: false
    }
  ],
  runtimeConfig: {
    public: {
      apiBase: ''
    }
  },
  css: ['~/assets/css/tailwind.css']
});
