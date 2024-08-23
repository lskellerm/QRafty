<script setup lang="ts">
// Extract the button size based on the screen width using the useButtonSize composable
const { buttonSize } = useButtonSize();

// State to track the
const isPasswordVisible = ref(false);

const togglePasswordVisibility = () => {
  /**
   * Function which toggles the visibility of the password field
   */
  isPasswordVisible.value = !isPasswordVisible.value;
};
</script>

<template>
  <Card
    class="flex flex-col px-9 py-2 justify-center items-center self-stretch bg-backgroundColor border-backgroundColor-400/35"
  >
    <CardHeader
      class="flex flex-col justify-center items-center gap-1 text-center py-4"
    >
      <NuxtImg src="/img/logos/logo-form-img.svg" width="45" height="45" />
      <CardTitle class="text-text font-heading text-2xl lg:text-3xl font-normal"
        >Create an account</CardTitle
      >
      <CardDescription
        class="text-primaryColor-400 font-sans text-xs lg:text-base lg:w-4/6"
        >Create an account to get started creating your custom QR codes today
        for free!
      </CardDescription>
    </CardHeader>
    <CardContent class="px-2 py-5 w-full">
      <form
        novalidate
        class="flex flex-col justify-center items-center px-3 py-0 gap-4"
      >
        <FormField v-slot="{ componentField }" name="name">
          <FormItem class="w-11/12">
            <FormLabel for="name" class="font-sans text-text text-sm"
              >Name</FormLabel
            >
            <FormControl>
              <Input
                class="font-sans text-sm placeholder:text-slate-400"
                type="text"
                v-bind="componentField"
                placeholder="John"
                name="name"
              />
            </FormControl>
          </FormItem>
        </FormField>
        <FormField v-slot="{ componentField }" name="username">
          <FormItem class="w-11/12">
            <FormLabel for="username" class="font-sans text-text text-sm"
              >Username</FormLabel
            >
            <FormControl>
              <Input
                class="font-sans text-sm placeholder:text-slate-400"
                type="text"
                v-bind="componentField"
                placeholder="yourusername123"
                name="username"
              />
            </FormControl>
          </FormItem>
        </FormField>
        <FormField v-slot="{ componentField }" name="email">
          <FormItem class="w-11/12">
            <FormLabel for="email" class="font-sans text-text text-sm"
              >Email</FormLabel
            >
            <FormControl>
              <div class="relative items-center w-full">
                <Input
                  class="font-sans text-sm pl-8 placeholder:text-slate-400"
                  type="email"
                  v-bind="componentField"
                  placeholder="m@example.com"
                  name="email"
                />
                <span class="absolute start-0 inset-y-0 flex items-center px-2">
                  <Icon
                    name="i-material-symbols-mail-outline"
                    class="bg-slate-400"
                    size="1.5rem"
                  />
                </span>
              </div>
            </FormControl>
          </FormItem>
        </FormField>
        <FormField v-slot="{ componentField }" name="password">
          <FormItem class="mt-2 w-11/12">
            <div class="flex justify-between items-center self-stretch">
              <FormLabel for="password" class="font-sans text-text text-sm"
                >Password</FormLabel
              >
              <div class="flex justify-center items-center gap-x-2">
                <Button
                  variant="icon"
                  size="icon"
                  aria-label="Toggle password visibility"
                  :aria-pressed="isPasswordVisible"
                  @click="togglePasswordVisibility"
                >
                  <Icon
                    name="i-material-symbols-visibility-off-rounded"
                    size="1rem"
                    class="bg-text"
                  />
                </Button>

                <span class="text-text font-sans text-sm">Hide</span>
              </div>
            </div>
            <FormControl>
              <Input
                class="font-sans text-sm placeholder:text-slate-400"
                :type="isPasswordVisible ? 'text' : 'password'"
                v-bind="componentField"
                name="password"
              />
            </FormControl>
          </FormItem>
        </FormField>
        <FormField
          v-slot="{ componentField }"
          name="agreeToTerms"
          type="checkbox"
        >
          <FormItem
            class="flex items-center p-2 pr-0 self-stretch gap-2 lg:ml-6 3xl:ml-8"
          >
            <FormControl>
              <Checkbox
                v-bind="componentField"
                id="agreeToTerms"
                class="text-primaryColor-400 lg:mt-1"
                name="agreeToTerms"
              >
              </Checkbox>
            </FormControl>
            <FormDescription
              class="text-text font-sans text-xs font-normal lg:text-sm"
            >
              By creating an account, you agree to our
              <NuxtLink to="/terms" class="underline"
                >Terms and Conditions</NuxtLink
              >
            </FormDescription>
          </FormItem>
        </FormField>
        <Button
          type="submit"
          :size="buttonSize"
          class="bg-secondaryColor w-11/12 rounded-3xl font-heading text-white"
          >Create an account</Button
        >
      </form>
    </CardContent>
  </Card>
</template>
