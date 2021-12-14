import random

import pytest
from selenium.webdriver.chrome import webdriver

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage:

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

    @staticmethod
    def random_num2():
        """Generate random number"""
        return str(random.choice(range(11, 99)))

    @pytest.fixture(scope="function")
    def driver(self):
        """Create and return driver, close after test"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def registered_user(self, start_page):
        """Register user and return data"""
        username_value = f"Name{self.random_num()}"
        email_value = f"user{self.random_num()}@mail.com"
        password_value = f"PassWord{self.random_num()}"
        # Fill email, login and password fields
        main_page = start_page.register_user(username_value, email_value, password_value)
        # Logout
        main_page.logout()
        return username_value, email_value, password_value

    def test_start_invalid(self, start_page):
        """
        - Create driver
        - Open start page
        - Find Username field
        - Put value
        - Find Password field
        - Put value
        - Click on Sign In button
        - Verify error message
        """
        start_page.login("bnmun", "jklkpw")
        start_page.verify_incorrect_login()

    def test_empty_fields_login(self, start_page):
        """
        - Create driver
        - Open start page
        - Find Username field
        - Find Password field
        - Click on Sign In button
        - Verify error message
        """
        start_page.login("", "")
        start_page.verify_incorrect_login()

    def test_register(self, start_page):
        """
        - Create driver
        - Open start page
        - Find Username field
        - Put value
        - Find Email field
        - Put value
        - Find Password field
        - Put value
        - Click on 'Sign up for OurApp' button
        - Verify Hello message
        """
        username_value = f'username{self.random_num()}'
        email_value = f'email{self.random_num()}@mail.com'
        password_value = f'Password{self.random_num()}'

        main_page = start_page.register_user(username_value, email_value, password_value)
        main_page.verify_welcome_message(username_value)

    def test_success_login(self, start_page, registered_user):
        """Pre-conditions:
            - Open start page
            - Register user
        - Steps:
            - Login as registered user
            - Verify welcome message"""
        username_value, _, password_value = registered_user
        main_page = start_page.login(username_value, password_value)
        main_page.verify_welcome_message(username_value)

    def test_check_title(self, start_page):
        """Verify that title ‘Complex app for testing – QA’ is present on top of the page"""
        start_page.verify_title()

    def test_check_username(self, start_page):
        """Verify that the required value for in ‘Username’ fields is more than 3 symbols"""

        un = f"N{self.random_num2()}"
        email = f"user{self.random_num2()}@mail.com"

        start_page.register_user("tt", email, "password1245667")
        start_page.verify_username_error()

        main_page = start_page.register_user(un, email, "password1245667")
        main_page.verify_welcome_message(un)

    @pytest.mark.parametrize("email", ["email", "email@"])
    def test_check_email(self, start_page, email):
        """Verify that email format ‘ad@gmail.com’ is allowed for the ‘Email’ field"""
        # email without '@mail.com and mail.com'
        start_page.input_email(email)
        start_page.verify_email_error()

    @pytest.mark.parametrize("email", ["email@mail", "email@mail."])
    def test_check_email2(self, start_page, email):
        """Verify that email format ‘ad@gmail.com’ is allowed for the ‘Email’ field"""
        # email without '.com and com'
        # un = f"Name{self.random_num()}"
        start_page.register_user("Blabla9874w", email, "Password12345")
        start_page.verify_email_error2()

    def test_password(self, start_page):
        """Verify that the required value for in ‘Password’ fields are 12 or more symbols """
        start_page.input_password('Password123')
        start_page.verify_password_error()
        # valid password is checked in test_register

    def test_sign_up_button(self, start_page):
        """ Verify that ‘Sign up for OurApp’ button is present under required fields """
        start_page.verify_sign_up_button()
        