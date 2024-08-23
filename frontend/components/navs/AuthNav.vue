<script setup lang="ts">
// Extract the button size based on the screen width using the useButtonSize composable
const { buttonSize } = useButtonSize();
</script>

<template>
  <div class="flex justify-end items-center self-stretch">
    <div class="flex justify-center items-center gap-3">
      <p class="font-sans text-xs lg:text-lg not-italic font-normal">
        Already have an account?
      </p>
      <Button variant="default" :size="buttonSize">Log in </Button>
    </div>
  </div>
</template>
