import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


def random_num():
    """Generate random number"""
    return str(random.choice(range(11111, 99999)))


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
