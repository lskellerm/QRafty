// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    strict: true,
    typeCheck: true
  },
  modules: ["@nuxtjs/eslint-module", "@nuxtjs/tailwindcss"],
  tailwindcss: {
    editorSupport: true
  }
});
