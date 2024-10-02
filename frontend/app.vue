<script setup lang="ts">
useHead({
  /* v8 ignore next 3 */
  titleTemplate: (titleChunk) => {
    return titleChunk ? `${titleChunk} | QRafty` : 'QRafty';
  }
});

/* Set up global registration state for usersto track the registration status across components and sign up worfklow
   ensuring it is only called once during SSR and client side navigation
*/

const isRegistered = useState('registered');

await callOnce(async () => {
  isRegistered.value = false;
});
</script>

<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
