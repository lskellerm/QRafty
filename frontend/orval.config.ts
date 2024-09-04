import { defineConfig } from 'orval';

export default defineConfig({
  qrafty: {
    input: {
      target: '../openapi.json',
      validation: true
    },
    output: {
      workspace: 'api/',
      mode: 'tags-split',
      target: './clients',
      client: 'fetch',
      prettier: true,
      override: {
        useTypeOverInterfaces: true,
        mutator: {
          path: '../composables/useAPI.ts',
          name: 'useAPI'
        },
        title: (title) => {
          return title.replace(title, 'QRafty');
        }
      }
    },
    hooks: {
      afterAllFilesWrite: 'prettier --write'
    }
  }
});
