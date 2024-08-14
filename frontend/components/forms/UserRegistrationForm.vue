<script lang="ts">
import { useForm } from 'vee-validate';
import { toTypedSchema } from '@vee-validate/zod';
import * as z from 'zod';

// Define the User Registration form schema using vee-validate/zod to integrate with Zod schema validation
const formSchema = toTypedSchema(
  z.object({
    email: z.string().email(),
    name: z.string().max(5),
    username: z.string().max(8),
    password: z.string().min(8)
  })
);

// Create the User Registration form using vee-validate useForm composable
const form = useForm({
  validationSchema: formSchema
});

// eslint-disable-next-line
const onSubmit = form.handleSubmit((values) => {
  /**
   * Submission handler for the User Registration form'
   * @param {Object} values - The user submitted form values
   */
  console.log('Form Submitted!', values);
  // TODO: Submit the form data to the serve using actual API call
});
</script>

<template>
  <Card
    class="flex flex-col px-10 py-5 justify-center items-center gap-5 self-stretch bg-backgroundColor border-backgroundColor-400/35"
  >
    <CardHeader class="text-center">
      <CardTitle>Create an account</CardTitle>
      <CardDescription
        >Create an account to get started creating your custom QR codes today
        for free!</CardDescription
      >
    </CardHeader>
  </Card>
  <!-- <form @submit="onSubmit">
    <FormField v-slot="{ nameField }" name="name">
      <FormItem>
        <FormLabel>Name</FormLabel>
        <FormControl>
          <Input type="text" v-bind="nameField" placeholder="John" />
        </FormControl>
      </FormItem>
    </FormField>
    <FormField v-slot="{ usernameField }" name="username">
      <FormItem>
        <FormLabel>Username</FormLabel>
        <FormControl>
          <Input
            type="text"
            v-bind="usernameField"
            placeholder="yourusername123"
          />
        </FormControl>
      </FormItem>
    </FormField>
    <FormField v-slot="{ emailField }" name="email">
      <FormItem>
        <FormLabel>Email</FormLabel>
        <FormControl>
          <Input type="email" v-bind="emailField" placeholder="m@example.com" />
        </FormControl>
      </FormItem>
    </FormField>
    <FormField v-slot="{ passwordField }" name="password">
      <FormItem>
        <FormLabel>Password</FormLabel>
        <FormControl>
          <Input type="password" v-bind="passwordField" />
        </FormControl>
      </FormItem>
    </FormField>
    <Button size="lg" class="bg-secondaryColor">Submit</Button>
  </form> -->
</template>
