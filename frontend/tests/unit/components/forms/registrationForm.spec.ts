import { describe, expect, test } from 'vitest';
import { mountSuspended } from '@nuxt/test-utils/runtime';
import { flushPromises } from '@vue/test-utils';
import UserRegistrationForm from '~/components/forms/UserRegistrationForm.vue';
import Button from '~/components/ui/button/Button.vue';
import FormMessage from '~/components/ui/form/FormMessage.vue';
import Input from '~/components/ui/input/Input.vue';
import Checkbox from '~/components/ui/checkbox/Checkbox.vue';

describe('User Registration Form Renders and Behaves Correctly', () => {
  test('renders registration form correctly', async () => {
    const wrapper = await mountSuspended(UserRegistrationForm, {
      attachTo: document.body
    });
    expect(wrapper.getComponent({ name: 'CardTitle' }).text()).toBe(
      'Create an account'
    );

    expect(wrapper.findAllComponents(Button)).toHaveLength(2);
    expect(wrapper.find('form').exists()).toBe(true);
    expect(wrapper.findAllComponents(Input)).toHaveLength(4);
    expect(wrapper.findAllComponents(Checkbox)).toHaveLength(1);

    wrapper.unmount();
  });

  test('password visibility toggles correctly when button is clicked', async () => {
    const wrapper = await mountSuspended(UserRegistrationForm);

    // Baseline sanity checks for the password input
    const passwordInput = wrapper.find('input[type="password"]');
    expect(passwordInput.exists()).toBe(true);

    // Assert that the password input is hidden by default, denoted by the type attribute
    expect(passwordInput.attributes('type')).toBe('password');

    // Trigger the click event on the password visibility button
    const passwordVisibilityButton = wrapper.findAllComponents(Button)[0];
    await passwordVisibilityButton.trigger('click');

    // First assert that a click event was emitted
    expect(passwordVisibilityButton.emitted('click')).toHaveLength(1);
    expect(passwordVisibilityButton.emitted()).toHaveProperty('click');

    // Now check that the password input is visible, denoted by the type attribute, being 'text'
    expect(passwordInput.attributes('type')).toBe('text');
  });

  test('creating account button is not visibile if submission is not in process', async () => {
    const wrapper = await mountSuspended(UserRegistrationForm, {
      attatchTo: document.body
    });
    expect(wrapper.findComponent('#loading-button').exists()).toBe(false);
  });

  test('creating account button is visible if submission is in process', async () => {
    const wrapper = await mountSuspended(UserRegistrationForm, {
      attachTo: document.body
    });

    // Set the values of all the form input fields
    await wrapper.findAllComponents(Input)[0].setValue('Luis Kellermann');
    await wrapper.findAllComponents(Input)[1].setValue('lskellermann123');
    await wrapper
      .findAllComponents(Input)[2]
      .setValue('MySuperStrongPassword123!');
    await wrapper.findComponent(Checkbox).setValue(true);
    await wrapper.findComponent(Checkbox).trigger('update:checked');

    // Simulate form submission by triggering a click event on the submit button
    const createAccountButton = wrapper.findAllComponents(Button)[1];
    await createAccountButton.trigger('click');

    // Flush all pending promises, needed for async validation performed by vee-validate
    await flushPromises();

    expect(createAccountButton.exists()).toBe(false);

    // Verify that the loading button is visible
    const loadingButton = wrapper.findComponent('#loading-button');
    expect(loadingButton.exists()).toBe(true);
    expect(loadingButton.text()).not.toBe('Create account');
    expect(loadingButton.text()).toBe('Creating account');
  });

  test("doesn't allow empty form submission", async () => {
    // Mount the component and attach it to the document body
    const wrapper = await mountSuspended(UserRegistrationForm, {
      attachTo: document.body
    });

    // Simulate form submission by triggering a click event on the submit button
    const createAccountButton = wrapper.findAllComponents(Button)[1];
    await createAccountButton.trigger('click');

    // Flush all pending promises, needed for async validation performed by vee-validate
    await flushPromises();

    // First assert that a click event was emitted by the form submission button
    expect(createAccountButton.emitted('click')).toHaveLength(1);
    expect(createAccountButton.emitted()).toHaveProperty('click');

    // Finally assert that a submission event was not emitted
    expect(wrapper.emitted('submit')).toBeUndefined();
    expect(wrapper.emitted()).not.toHaveProperty('submit');

    // Verify that error messages are displayd for each input field
    const errorMessages = wrapper.findAllComponents(FormMessage);

    expect(errorMessages).toHaveLength(5);

    // Unmount the component from the document body
    wrapper.unmount();
  });
});
