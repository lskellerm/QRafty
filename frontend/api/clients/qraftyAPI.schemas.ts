/**
 * Generated by orval v7.0.1 🍺
 * Do not edit manually.
 * QRafty API
 * QRafty API helps to manage and create QR codes, allowing the user to create, edit and delete fully custom QR codes.
 * OpenAPI spec version: 0.1.0
 */
export type ValidationErrorLocItem = string | number;

export type ValidationError = {
  loc: ValidationErrorLocItem[];
  msg: string;
  type: string;
};

/**
 * Pydantic model for reading User data, used for serialization and response payloads

Args:
    schemas (BaseUser): FastAPI_Users BaseUser Pydantic model provided as a mixin
 */
export type UserRead = {
  email: string;
  id: string;
  is_active?: boolean;
  is_superuser?: boolean;
  is_verified?: boolean;
  /**
   * Name of the User being read
   * @maxLength 30
   */
  name: string;
  /**
   * User's display name
   * @maxLength 30
   */
  username: string;
};

export type UserCreateIsVerified = boolean | null;

export type UserCreateIsSuperuser = boolean | null;

export type UserCreateIsActive = boolean | null;

/**
 * Pydantic model for creating User data, dedicated to User registration,
consisting of mandatory password email and password field.

Args:
    schemas (BaseUserCreate): FastAPI_Users BaseUserCreate Pydantic model provided as a mixin
 */
export type UserCreate = {
  email: string;
  is_active?: UserCreateIsActive;
  is_superuser?: UserCreateIsSuperuser;
  is_verified?: UserCreateIsVerified;
  /**
   * Name of the User being created
   * @minLength 2
   * @maxLength 30
   */
  name: string;
  password: string;
  /**
   * User's display name
   * @minLength 2
   * @maxLength 30
   */
  username: string;
};

export type HTTPValidationError = {
  detail?: ValidationError[];
};

export type ErrorModelDetailAnyOf = { [key: string]: string };

export type ErrorModelDetail = string | ErrorModelDetailAnyOf;

export type ErrorModel = {
  detail: ErrorModelDetail;
};
