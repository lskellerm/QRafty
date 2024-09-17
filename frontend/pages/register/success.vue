<script setup lang="ts">
definePageMeta({
  layout: 'message',
  middleware: [
    /*
      Navigation guard to prevent the user from directly accessing the page,
      only allowing routing from the register page the first time the user registers
    */
    function () {
      // Get the register state from the registered state
      const isRegistered = useState<boolean>('registered');
      if (!isRegistered.value) {
        return navigateTo('/register');
      }
    }
  ],
  layoutTransition: {
    name: 'fade-scale',
    mode: 'out-in',
    type: 'transition'
  }
});

useServerSeoMeta({
  title: 'Sign up Successful!',
  ogTitle: 'Sign up Successful!',
  robots: 'noindex, nofollow',
  description: 'Congratulations, your account has been created!',
  ogDescription: 'Congratulations, your account has been created!'
});

// Import the useButtonSize composable
const { buttonSize } = useButtonSize();

// Clear the registered state to prevent the user from accessing the page again
onBeforeRouteLeave(() => {
  clearNuxtState('registered');
});
</script>

<template>
  <div class="flex justify-center items-center p-2 lg:w-2/5 3xl:w-1/4 lg:p-4">
    <Card
      class="flex flex-col justify-center items-center w-11/12 bg-backgroundColor border-backgroundColor-400/35 py-2 lg:p-10"
    >
      <CardHeader
        class="flex flex-col justify-center items-center gap-4 pb-3 lg:pb-5"
      >
        <Icon
          name="i-lucide-circle-check-big"
          mode="css"
          class="bg-secondaryColor self-center"
          size="10rem"
        />
        <CardTitle
          class="text-center font-heading text-2xl lg:text-4xl font-normal"
          >Success
        </CardTitle>
        <CardDescription
          class="text-center text-primaryColor-400 font-sans text-sm lg:text-xl w-full"
          >Congratulations, your account has been created!</CardDescription
        >
      </CardHeader>
      <CardContent
        class="flex flex-col align-center justify-center text-center gap-y-5 lg:gap-y-7 lg:px-2 lg:w-full"
      >
        <p class="text-primaryColor-400 text-sm lg:text-base">
          An email has been sent, check your
          <span class="font-semibold text-accentColor italic">email</span> to
          verify and get started using your account
        </p>
        <Button
          type="buton"
          :size="buttonSize"
          variant="default"
          class="w-3/4 rounded-3xl font-heading font-semibold self-center lg:text-xl lg:p-6"
          >Sign in</Button
        >
      </CardContent>
    </Card>
  </div>
</template>

<style>
.fade-scale-enter-active,
.fade-scale-leave-active {
  transition: all 0.4s ease;
}

.fade-scale-enter-from,
.fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

.fade-scale-enter-to,
.fade-scale-leave-from {
  opacity: 1;
  transform: scale(1);
}
</style>
