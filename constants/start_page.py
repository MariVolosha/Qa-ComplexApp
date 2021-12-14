class StartPageConstants:
    # SIGN IN
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[contains(text(), 'Sign In')]"
    SIGN_IN_ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_ERROR_MESSAGE_TEXT = "Error"
    # SIGN UP
    SIGN_UP_USERNAME_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    # TITLE
    START_TITLE_XPATH = ".//h4"
    # ERRORS
    SIGN_IN_USERNAME_ERROR = ".//div[@class='alert alert-danger small']"
    SIGN_IN_EMAIL_ERROR = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
    SIGN_IN_EMAIL_ERROR2 = ".//div[@class='alert alert-danger small']"
    SIGN_IN_PASSWORD_ERROR = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
    SIGN_IN_ERROR_PASSWORD_TEXT = "Password must be at least 12 characters."
