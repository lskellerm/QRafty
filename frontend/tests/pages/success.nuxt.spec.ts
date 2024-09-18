import { describe, test, expect, afterEach } from 'vitest';
import { mountSuspended } from '@nuxt/test-utils/runtime';
import App from '~/app.vue';

describe('Success Page', () => {
  afterEach(() => {
    // Invalidate the cached registration state after each test
    clearNuxtState('registered');
  });
  test('redirect an unregistered user back to the registration page', async () => {
    const wrapper = await mountSuspended(App, { route: '/register/success' });
    expect(wrapper.getComponent({ name: 'UserRegistrationForm' }));
    expect(wrapper.html()).not.toContain('Success');
    expect(wrapper.html()).toContain('Create an account');
  });

  test('route a registered user to the success page', async () => {
    // Set the registration state to true
    useState('registered').value = true;
    const wrapper = await mountSuspended(App, { route: '/register/success' });
    expect(wrapper.html()).toContain('Success');
    expect(wrapper.html()).not.toContain('Create an account');
  });
});
