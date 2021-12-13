from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def login(self, username_value, password_value):
        """Login using provided password and username"""
        from pages.main_page import MainPage
        # Clear required fields and fill
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username_value)
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password_value)
        self.log.debug("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click()
        self.log.debug("Clicked on 'Sign In'")
        return MainPage(self.driver)

    def verify_incorrect_login(self):
        """Verify error message on invalid login"""
        # Find error message
        message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        # Verify message
        assert message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT

    def register_user(self, username_value, email_value, password_value):
        """Register user using provided data"""
        from pages.main_page import MainPage
        # Fill email
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_USERNAME_XPATH, value=username_value)
        # Fill email
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_EMAIL_XPATH, value=email_value)
        # Fill password
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_PASSWORD_XPATH, value=password_value)
        self.log.debug("Fields were filled")
        sleep(1)
        # Click on Sign Up button
        self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_BUTTON_XPATH).click()
        sleep(1)
        self.log.debug("User was registered")
        return MainPage(self.driver)

    def input_email(self, email_value):
        from pages.main_page import MainPage
        # Fill email
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_EMAIL_XPATH, value=email_value)
        sleep(2)
        self.log.debug("User was registered")
        return MainPage(self.driver)

    def input_password(self, password_value):
        from pages.main_page import MainPage
        # Fill password
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_PASSWORD_XPATH, value=password_value)
        sleep(2)
        return MainPage(self.driver)

    def verify_title(self):
        """Verify that title ‘Complex app for testing – QA’ is present on top of the page"""
        title = self.driver.find_element(by=By.XPATH, value=self.constants.START_TITLE_XPATH)
        assert title.is_enabled()

    def verify_username_error(self):
        message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_USERNAME_ERROR)
        assert message.text == "Username must be at least 3 characters."

    def verify_email_error(self):
        message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_EMAIL_ERROR)
        assert message.text == "You must provide a valid email address."

    def verify_email_error2(self):
        message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_EMAIL_ERROR2)
        assert message.text == "You must provide a avalid email address."

    def verify_password_error(self):
        message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_PASSWORD_ERROR)
        assert message.text == self.constants.SIGN_IN_ERROR_PASSWORD_TEXT

    def verify_sign_up_button(self):
        button = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_BUTTON_XPATH)
        assert button.is_enabled()
