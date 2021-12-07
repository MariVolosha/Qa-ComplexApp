import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


def random_num():
    """Generate random number"""
    return str(random.choice(range(11111, 99999)))


def random_num2():
    """Generate random number"""
    return str(random.choice(range(11, 99)))


class TestStartPage:

    def test_start_page(self):
        """Sample test"""
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert message.text == "Error"

    def test_start_invalid(self):
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
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys(f'Username{random_num()}')
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(f'pwd{random_num()}')
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert message.text == "Error"

    def test_register(self):
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
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # name
        username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
        username.clear()
        user_text = (f'username{random_num()}')
        username.send_keys(user_text)
        # email
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        email.clear()
        email.send_keys(f'email{random_num()}@mail.com')
        # password
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        password.send_keys(f'password{random_num()}')
        # button
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sleep(2)
        button.click()
        sleep(2)
        hello = driver.find_element(by=By.XPATH, value=".//H2")
        assert hello.text == f'Hello {user_text}, your feed is empty.'

    def test_check_title(self):
        """Verify that title ‘Complex app for testing – QA’ is present on top of the page"""
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        title = driver.find_element(by=By.XPATH, value=".//h4")
        assert title.is_enabled()

    def test_check_username(self):
        """Verify that the required value for in ‘Username’ fields is more than 3 symbols"""
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
        username.clear()
        username.send_keys(f'{random_num2()}')
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        email.clear()
        email.send_keys(f'email{random_num()}@mail.com')
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        password.send_keys(f'password{random_num()}')
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sleep(2)
        button.click()
        sleep(2)
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small']")
        assert message.text == "Username must be at least 3 characters."

        username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
        user_text = (f'p{random_num2()}')
        username.clear()
        username.send_keys(user_text)
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        email.clear()
        email.send_keys(f'email{random_num()}@mail.com')
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        password.send_keys(f'password{random_num()}')
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sleep(2)
        button.click()
        sleep(2)
        hello = driver.find_element(by=By.XPATH, value=".//H2")
        assert hello.text == f'Hello {user_text}, your feed is empty.'

    def test_check_email(self):
        """Verify that email format ‘ad@gmail.com’ is allowed for the ‘Email’ field"""
        # email without '@mail.com'
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        email.clear()
        email.send_keys(f'email{random_num()}')
        sleep(3)
        message = driver.find_element(by=By.XPATH,
                                      value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert message.text == "You must provide a valid email address."
        # email without 'mail.com'
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        email.clear()
        email.send_keys(f'email{random_num()}@')
        sleep(3)
        message = driver.find_element(by=By.XPATH,
                                      value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert message.text == "You must provide a valid email address."
        # email without '.com'
        username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
        username.clear()
        username.send_keys(f'name{random_num()}')
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        email.clear()
        email.send_keys(f'email{random_num()}@mail')
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        password.send_keys(f'password{random_num()}')
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sleep(2)
        button.click()
        sleep(2)
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small']")
        assert message.text == "You must provide a avalid email address."
        # email without 'com'
        username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
        username.clear()
        username.send_keys(f'name{random_num()}')
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        email.clear()
        email.send_keys(f'email{random_num()}@mail.')
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        password.send_keys(f'password{random_num()}')
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sleep(2)
        button.click()
        sleep(2)
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small']")
        assert message.text == "You must provide a avalid email address."
        # valid email is checked in test_register

    def test_password(self):
        """Verify that the required value for in ‘Password’ fields are 12 or more symbols """
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # password 11 symbols
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        password.send_keys(f'password123')
        sleep(3)
        message = driver.find_element(by=By.XPATH,
                                      value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert message.text == "Password must be at least 12 characters."
        # valid password is checked in test_register

    def test_sign_up_button(self):
        """ Verify that ‘Sign up for OurApp’ button is present under required fields """
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        assert button.is_enabled()
