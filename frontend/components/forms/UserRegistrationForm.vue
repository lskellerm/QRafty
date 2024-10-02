<script setup lang="ts">
import { useForm } from 'vee-validate';
import { toTypedSchema } from '@vee-validate/zod';
import { vAutoAnimate } from '@formkit/auto-animate';
import type { FetchError } from 'ofetch';
import * as z from 'zod';

// Regex pattern search for a password with at least 1 uppercase letter, 1 digit, 1 special character and a minimum length of 8 characters
const PATTERN = /^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])(?!.*\s).{8,}$/;

// Define the User Registration form schema using vee-validate/zod to integrate with Zod schema validation
const formSchema = toTypedSchema(
  z
    .object({
      name: z
        .string({
          required_error: 'Name is required'
        })
        .min(1, {
          message: 'Name is required'
        })
        .min(2, {
          message: 'Name must be at least 2 characters long'
        })
        .max(30, {
          message: 'Name must be less than 30 characters long'
        }),
      username: z
        .string({
          required_error: 'Username is required'
        })
        .min(1, {
          message: 'Username is required'
        })
        .min(2, {
          message: 'Username must be at least 2 characters long'
        })
        .max(30, {
          message: 'Username must be less than 30 characters long'
        }),
      email: z
        .string()
        .min(1, {
          message: 'Email is required'
        })
        .email({ message: 'Invalid email address' }),
      password: z
        .string({
          required_error: 'Password is required'
        })
        .min(8, {
          message: 'Password must be at least 8 characters long'
        })
        .min(1, {
          message: 'Password is required'
        })
        .regex(PATTERN, {
          message:
            'Password must contain at least 1 uppercase letter, 1 digit, 1 special character and no spaces'
        }),
      agreeToTerms: z
        .boolean({
          required_error: 'You must agree to the terms and conditions'
        })
        .refine(
          (value) => {
            return value === true;
          },
          {
            message: 'You must agree to the terms and conditions'
          }
        )
        .default(false)
    })
    .required()
);

/* Extract the handleSubmit, isSubmitting state, from the useForm composable to handle form submission and validation,
   while also providing the initial values for the form fields, set to undefined to catch fields which are not filled in.
*/
const { handleSubmit, isSubmitting, handleReset, setFieldError } = useForm({
  validationSchema: formSchema,
  initialValues: {
    name: undefined,
    username: undefined,
    email: undefined,
    password: undefined,
    agreeToTerms: undefined
  }
});

const submitForm = handleSubmit(async (values) => {
  /**
   * Submission handler for the User Registration form, using the handleSubmit function from the Vee-validate useForm composable
   * @param {Object} values - The user submitted form values
   */
  // Create a new object to exclude agreeToTerms from payload
  const { agreeToTerms, ...submissionValues } = values; // eslint-disable-line no-unused-vars
  try {
    const response = await authRegister(submissionValues);
    if (response.status === 201) {
      // Reset the form fields
      handleReset();

      // Redirect the user to the registration success page and set the registered state to true
      useState('registered').value = true;
      await navigateTo('/register/success');
    }
  } catch (error) {
    //  Assert the error response type to be a generic FetchError with a union type of HTTPValidationError or ErrorModel
    const errorResponse = error as FetchError<HTTPValidationError | ErrorModel>;
    /*
       Handle different error types and set the field error message accordingly using type guards

       Error types can be:
         - HTTPValidationError (Server validation error for missing required fields)
         - ErrorModel (Server validation error for user with existing email and/or username or invalid password format)
    */

    // Check if it's a generic error response, denoting a server validation error against database constraints
    if (isErrorModel(errorResponse.data)) {
      const serverValidationError = errorResponse.data as ErrorModel;
      if (typeof serverValidationError?.detail === 'string') {
        setFieldError(
          'email',
          'User with this email already exists, please register using a different email'
        );
      } else if (typeof serverValidationError?.detail === 'object') {
        if (
          serverValidationError.detail?.code ===
          'REGISTER_USERNAME_ALREADY_EXISTS'
        ) {
          setFieldError('username', serverValidationError.detail.reason);
        }
        if (
          serverValidationError.detail?.code === 'REGISTER_INVALID_PASSWORD'
        ) {
          setFieldError('password', serverValidationError.detail.reason);
        }
      }
    }
    // Otherwise check for an HTTPValidationError response, denoting a server validation error for missing required fields
    else if (isHTTPValidationError(errorResponse.data)) {
      const requieredValidationError =
        errorResponse.data as HTTPValidationError;

      requieredValidationError.detail?.forEach((error) => {
        if (error.loc[1] === 'name') {
          setFieldError('name', error.msg);
        }
        if (error.loc[1] === 'username') {
          setFieldError('username', error.msg);
        }
        if (error.loc[1] === 'email') {
          setFieldError('email', error.msg);
        }
        if (error.loc[1] === 'password') {
          setFieldError('password', error.msg);
        }
      });
    }
  }
});

// Extract the button size based on the screen width using the useButtonSize composable
const { buttonSize } = useButtonSize();

// State to track the visibility of the password field
const isPasswordVisible = ref(false);

const togglePasswordVisibility = () => {
  /**
   * Function which toggles the visibility of the password field
   */
  isPasswordVisible.value = !isPasswordVisible.value;
};
</script>

<template>
  <div>
    <Card
      class="flex flex-col px-9 py-2 justify-center items-center self-stretch bg-backgroundColor border-backgroundColor-400/35"
    >
      <CardHeader
        class="flex flex-col justify-center items-center gap-1 text-center py-4"
      >
        <NuxtImg src="/img/logos/logo-form-img.svg" width="45" height="45" />
        <CardTitle
          class="text-text font-heading text-2xl lg:text-3xl font-normal"
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
          id="user-registration-form"
          novalidate
          class="flex flex-col justify-center items-center px-3 py-0 gap-4"
          @submit.prevent="submitForm"
          @keydown.enter="$event.preventDefault()"
        >
          <FormField v-slot="{ componentField }" name="name">
            <FormItem v-auto-animate class="w-11/12">
              <FormLabel for="name" class="font-sans text-text text-sm"
                >Name</FormLabel
              >
              <FormControl>
                <Input
                  class="font-sans text-sm placeholder:text-slate-400"
                  type="text"
                  v-bind="componentField"
                  placeholder="John"
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>
          <FormField v-slot="{ componentField }" name="username">
            <FormItem v-auto-animate class="w-11/12">
              <FormLabel for="username" class="font-sans text-text text-sm"
                >Username</FormLabel
              >
              <FormControl>
                <Input
                  class="font-sans text-sm placeholder:text-slate-400"
                  type="text"
                  v-bind="componentField"
                  placeholder="yourusername123"
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>
          <FormField v-slot="{ componentField }" name="email">
            <FormItem v-auto-animate class="w-11/12">
              <FormLabel for="email" class="font-sans text-text text-sm"
                >Email</FormLabel
              >
              <FormControl>
                <div class="relative items-center w-full">
                  <Input
                    class="font-sans text-sm pl-8 placeholder:text-slate-400"
                    type="email"
                    v-bind="componentField"
                    placeholder="email@example.com"
                  />
                  <span
                    class="absolute start-0 inset-y-0 flex items-center px-2"
                  >
                    <Icon
                      name="i-material-symbols-mail-outline"
                      class="bg-slate-400"
                      size="1.5rem"
                    />
                  </span>
                </div>
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>
          <FormField v-slot="{ componentField }" name="password">
            <FormItem v-auto-animate class="w-11/12">
              <div class="flex justify-between items-center self-stretch">
                <FormLabel for="password" class="font-sans text-text text-sm"
                  >Password</FormLabel
                >
                <div class="flex justify-center items-center gap-x-0">
                  <Button
                    type="button"
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
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>
          <FormField
            v-slot="{ componentField, value, handleChange }"
            name="agreeToTerms"
            type="checkbox"
            ><FormItem
              v-auto-animate
              class="flex flex-col items-start p-2 self-stretch gap-2 lg:ml-4 2xl:ml-6 3xl:ml-8"
            >
              <div class="flex items-center">
                <FormControl>
                  <Checkbox
                    id="agreeToTerms"
                    type="checkbox"
                    class="text-primaryColor-400 mr-1"
                    v-bind="componentField"
                    :checked="value"
                    :value="value"
                    @update:model-value="handleChange"
                    @update:checked="handleChange"
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
              </div>
              <FormMessage class="w-full" />
            </FormItem>
          </FormField>
          <Button
            v-if="!isSubmitting"
            id="submit-button"
            type="submit"
            :size="buttonSize"
            :disabled="isSubmitting"
            class="bg-secondaryColor w-11/12 rounded-3xl font-heading text-white"
            @keydown.enter="submitForm"
            >Create an account</Button
          >
          <Button
            v-else
            id="loading-button"
            disabled
            type="submit"
            :size="buttonSize"
            class="bg-secondaryColor w-11/12 rounded-3xl font-heading text-white"
          >
            <Icon
              name="i-lucide-loader-circle"
              class="animate-spin bg-text-white mr-2"
              size="1.5rem"
            />
            Creating account
          </Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>
