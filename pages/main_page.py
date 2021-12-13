from selenium.webdriver.common.by import By

from constants.main_page import MainPageConstants
from pages.base import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def verify_welcome_message(self, username):
        """Verify welcome message for the user"""
        hello_message = self.driver.find_element(by=By.XPATH, value=self.constants.WELCOME_MESSAGE_XPATH)
        assert hello_message.text == f"Hello {username.lower()}, your feed is empty."

    def logout(self):
        """Sign out from user account"""
        self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_OUT_BUTTON_XPATH).click()
