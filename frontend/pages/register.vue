<script setup lang="ts">
import { definePageMeta } from '#imports';
import { useWindowSize } from '@vueuse/core';

// Defined the page metadata for the Register page
definePageMeta({
  layout: 'auth'
});

// Extract the width from the window size using the useWindowSize composable
const { width } = useWindowSize();

// Computed property to determine if the screen width is less than 768px, returns true if it is, false otherwise
const isMobile = computed(() => width.value <= 768);
</script>

<template>
  <div>
    <div class="flex-shrink-0 self-stretch">
      <NuxtImg
        v-if="!isMobile"
        src="/img/heros/desktop-register-hero.svg"
        sizes="100vw"
      />
      <NuxtImg
        v-if="isMobile"
        src="/img/heros/mobile-form-hero.svg"
        sizes="100vw"
      />
    </div>
    <div class="flex flex-col items-center gap-11 shrink-0 py-10 px-5">
      <AuthNav />
      <UserRegistrationForm />
    </div>
  </div>
</template>
