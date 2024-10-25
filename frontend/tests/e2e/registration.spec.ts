import { test, expect } from '@nuxt/test-utils/playwright';

const apiBaseUrl = process.env.CI
  ? 'http://localhost:8000'
  : 'http://backend:8000';

test.describe('User Registration Flow UI Correctly displays feedback and funtions properly', () => {
  /**
   * The following test suite performs UI testing against the User Registration Flow
   *
   * As a result, all API calls are mocked to return the appropriate responses for the test cases
   * to ensure that the UI is functioning correctly and displaying the appropriate feedback to the user
   *
   * The next test suite will perform end-to-end testing against the User Registration Flow with real API calls
   */
  test.beforeEach(async ({ goto }) => {
    await goto('/register', { waitUntil: 'hydration' });
  });
  test('Toggle Password Button Shows Password Correctly', async ({ page }) => {
    const togglePasswordButton = page.getByTestId('toggle-password-visibility');
    await expect(togglePasswordButton).toBeVisible();

    await togglePasswordButton.click();

    const passwordInput = page.getByTestId('password');

    expect(await passwordInput.getAttribute('type')).toBe('text');
  });

  test('should display server-side validation errors for passwords containing personally identifiable information ', async ({
    page
  }) => {
    // Mock the api call to return a 400 error and the appropriate error message
    await page.route('*/**/auth/register', async (route) => {
      const jsonResponse = {
        detail: {
          code: 'REGISTER_INVALID_PASSWORD',
          reason:
            'Password should not contain your email, username or name for security reasons'
        }
      };
      await route.fulfill({ json: jsonResponse, status: 400 });
    });

    // Fill the form with a duplicate username
    await page.getByPlaceholder('John').fill('John Doe');
    await page.getByPlaceholder('yourusername123').fill('newusername123');
    await page.getByPlaceholder('email@example.com').fill('test@example.com');
    await page.getByTestId('password').fill('JohnDoe123!');
    await page.getByRole('checkbox').check();

    // Submit the form
    const submitButton = page.getByTestId('submit-button');
    await submitButton.click();

    // Check for the server-side validation error message related to the duplicate email
    await expect(
      page.getByText(
        'Password should not contain your email, username or name for security reasons'
      )
    ).toBeVisible();
  });
});

test.describe('End-to-End User Registration Flow', () => {
  /**
   * The following test suite performs end-to-end testing against the User Registration Flow
   *
   * As a result, all API calls are made to the actual backend server to ensure that the User Registration Flow is functioning correctly
   *
   * A new API call is made before each test using the `beforeEach` hook to create an initial user in the database
   * and these users are cleaned up after all tests have been run using the `afterAll` hook
   * to ensure a clean state.
   */

  test.beforeEach(async ({ goto, request }) => {
    await goto('/register', { waitUntil: 'hydration' });

    // Create an initial user in the database
    const user: UserCreate = {
      email: 'JDoe@gmail.com',
      name: 'John Doe',
      password: 'MySuperStrongPassword123!',
      username: 'JDoe123'
    };

    await request.post(`${apiBaseUrl}/auth/register`, {
      data: user
    });
  });

  test.afterEach(
    'Delete the initial entry in the database used for testing',
    async ({ request }) => {
      // Delete the initial users created in the database, cleaning up the db state for the next test run
      const response = await request.delete(
        `${apiBaseUrl}/testing/users/JDoe123`
      );

      // Check if the response is successful or not found, denoting expected behavior
      expect(response.ok() || response.status() === 404).toBeTruthy();
    }
  );

  test('should display server-side validation error when duplicate username is provided', async ({
    page
  }) => {
    // Fill the form with a non-unique username
    await page.getByPlaceholder('John').fill('John D');
    await page.getByPlaceholder('yourusername123').fill('JDoe123');
    await page
      .getByPlaceholder('email@example.com')
      .fill('JDoe123@example.com');
    await page.getByTestId('password').fill('Password1231!');
    await page.getByRole('checkbox').check();

    // Submit the form
    const submitButton = page.getByTestId('submit-button');
    await submitButton.click();

    // Check for the server-side validation error message
    await expect(
      page.getByText(
        'A user with this username already exists, please register using a different username'
      )
    ).toBeVisible();
  });

  test('should display server-side validation error when duplicate email is provided', async ({
    page
  }) => {
    // Fill the form with a non-unique email
    await page.getByPlaceholder('John').fill('John D');
    await page.getByPlaceholder('yourusername123').fill('JDoeUsername');
    await page.getByPlaceholder('email@example.com').fill('JDoe@gmail.com');
    await page.getByTestId('password').fill('Password1231!');
    await page.getByRole('checkbox').check();

    // Submit the form
    const submitButton = page.getByTestId('submit-button');
    await submitButton.click();

    // Check for the server-side validation error message
    await expect(
      page.getByText(
        'User with this email already exists, please register using a different email'
      )
    ).toBeVisible();
  });

  test('should display server-side validation error when password contains personally identifiable information', async ({
    page
  }) => {
    // Fill the form with a duplicate username
    await page.getByPlaceholder('John').fill('John Doe');
    await page.getByPlaceholder('yourusername123').fill('newusername123');
    await page.getByPlaceholder('email@example.com').fill('test@example.com');
    await page.getByTestId('password').fill('JohnDoe123!');
    await page.getByRole('checkbox').check();

    // Submit the form
    const submitButton = page.getByTestId('submit-button');
    await submitButton.click();

    // Check for the server-side validation error message related to the duplicate email
    await expect(
      page.getByText(
        'Password should not contain your email, username or name for security reasons'
      )
    ).toBeVisible();
  });

  test('should successfully register a new user', async ({ page, request }) => {
    // Fill the form with a duplicate username
    await page.getByPlaceholder('John').fill('John doe');
    await page.getByPlaceholder('yourusername123').fill('JD03123');
    await page.getByPlaceholder('email@example.com').fill('JDoe1094@gmail.com');
    await page.getByTestId('password').fill('MySuperSecretPassword1!*');
    await page.getByRole('checkbox').check();

    // Submit the form
    const submitButton = page.getByTestId('submit-button');
    await submitButton.click();

    // Verify that the user is redirected to the successfull registration page
    await expect(page).toHaveURL('/register/success');
    await expect(
      page.getByText('Congratulations, your account has been created!')
    ).toBeVisible();

    await request.delete(`${apiBaseUrl}/testing/users/JD03123`);
  });
});
