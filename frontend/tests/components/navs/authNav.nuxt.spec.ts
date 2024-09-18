import { describe, test, expect } from 'vitest';
import { mountSuspended, mockNuxtImport } from '@nuxt/test-utils/runtime';
import AuthNav from '~/components/navs/AuthNav.vue';

// Mock the useButtonSize composable
mockNuxtImport('useButtonSize', () => {
  return () => {
    return { buttonSize: 'lg' };
  };
});

describe('AuthNav', () => {
  test('renders correctly', async () => {
    const wrapper = await mountSuspended(AuthNav);
    expect(wrapper.text()).toContain('Already have an account? Log in');
  });

  test('renders correctly with log in button', async () => {
    const wrapper = await mountSuspended(AuthNav);
    expect(wrapper.getComponent({ name: 'Button' }));
    expect(wrapper.getComponent({ name: 'Button' }).text()).toBe('Log in');
  });

  test('renders the correct button size using useButtonSize composable value (screen size)', async () => {
    const wrapper = await mountSuspended(AuthNav);
    const button = wrapper.findComponent({ name: 'Button' });

    expect(button.props().size).toBe('lg');
  });
});
