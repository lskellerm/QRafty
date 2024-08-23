import { computed } from 'vue';
import { useWindowSize } from '@vueuse/core';
import type { ButtonVariants } from '~/components/ui/button';

export function useButtonSize() {
  /**
   * Composable function used to determine the size of the button based on the window width which can be
   * used to dynamically adjust the size of the button based on the screen size.
   *
   * @returns {ButtonVariants['size']} The size of the button based on the screen width
   */

  // Extract the width from the useWindowSize vueuse composable
  const { width } = useWindowSize();

  // Check if the width is less than 768 pixels, denoting a mobile device
  const isMobile = computed<boolean>(() => width.value < 768);

  // Check if the screen width is greater than 1440 pixels, denoting a desktop device
  const isDesktop = computed<boolean>(() => width.value >= 1440);

  // Determine the size of the button based on the screen width,
  const buttonSize = computed<ButtonVariants['size']>(() =>
    isMobile.value ? 'xs' : isDesktop.value ? 'lg' : 'md'
  );

  return { buttonSize };
}
