<script lang="ts">
import { definePageMeta } from '#imports';
definePageMeta({
  layout: 'auth'
});
</script>

<template>
  <div>
    <div class="flex-shrink-0 self-stretch">
      <NuxtImg src="/img/heros/mobile-form-hero.svg" sizes="100vw" />
    </div>
    <div class="flex flex-col items-center gap-11 shrink-0 py-10 px-5">
      <AuthNav />
    </div>
    <UserRegistrationForm />
  </div>
</template>
