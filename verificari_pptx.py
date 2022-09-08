from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    LOGIN_LABEL = (By.XPATH, '//h2')
    USERNAME_INPUT = (By.XPATH, '//input[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button/i')
    ELEMENTAL_SELENIUM = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')
    LOGIN_ERROR = (By.XPATH, '//div[@class="flash error"]')
    X_LOGIN_ERROR = (By.XPATH, '//a[@class="close"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.implicitly_wait(5)
        self.chrome.find_element(By.XPATH, '(//a[text() = "Form Authentication"])').click()

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'The url is incorrect.')

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(actual, expected, 'The title is incorrect.')

    def test_xpath_element(self):
        actual = self.chrome.find_element(*self.LOGIN_LABEL).text
        expected = 'Login Page'
        self.assertEqual(actual, expected, 'The login label is incorrect.')

    def test_login_button_is_displayed(self):
        button = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(button.is_displayed(), 'The login button is not displayed.')

    def test_elem_href_selenium_is_correct(self):
        actual = self.chrome.find_element(*self.ELEMENTAL_SELENIUM).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual, expected, 'The link is incorrect.')

    def test_the_error_is_displayed(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = self.chrome.find_element(*self.LOGIN_ERROR)
        self.assertTrue(error.is_displayed(), 'The error is not displayed.')

    def test_the_error_message_is_correct(self):
        self.chrome.find_element(*self.USERNAME_INPUT).send_keys('Nicu')
        self.chrome.find_element(*self.PASSWORD_INPUT).send_keys('1234')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.LOGIN_ERROR).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is  incorrect.')

    def test_the_error_disappeared(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(3)
        self.chrome.find_element(*self.X_LOGIN_ERROR).click()
        sleep(1)
        try:
            self.chrome.find_element(*self.LOGIN_ERROR)
            raise Exception('The error message is still there.')
        except NoSuchElementException:
            pass

    def test_label_test(self):
        label_list = self.chrome.find_elements(By.XPATH, '//label')
        actual = label_list[0].text
        expected = 'Username'
        self.assertEqual(actual, expected, 'The username label is incorrect.')
        actual2 = label_list[1].text
        expected2 = 'Password'
        self.assertEqual(actual2, expected2, 'The password label is incorrect.')

    def test_has_secure_and_flash_succes_is_displayed(self):
        self.chrome.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD_INPUT).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.current_url
        expected = 'secure'
        self.assertTrue(expected in actual, 'The link doesn\'t contains "secure".')
        try:
            WebDriverWait(self.chrome, 5).\
                until(EC.presence_of_element_located((By.XPATH, '//div/div[@class="flash success"]')))
        except TimeoutException:
            self.assertTrue(False, 'I waited 5 seconds, but did not find the elem. "flash success".')
        element = self.chrome.find_element(By.XPATH, '//div/div[@class="flash success"]')
        self.assertTrue(element.is_displayed(), 'Nothing displayed.')
        actual2 = element.text
        expected2 = 'secure area'
        self.assertTrue(expected2 in actual2, 'The text does not contain "secure area".')

    def test_check_where_you_are(self):
        self.chrome.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD_INPUT).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(By.XPATH, '//i[@class="icon-2x icon-signout"]').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'The link is incorrect. You are in the wrong place.')

    @unittest.skip
    def test_brute_force_password_hacking(self):
        self.chrome.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        element = self.chrome.find_element(By.XPATH, '//h4[@class="subheader"]').text
        print(element)
        words = element.split(' ')
        print(words)
        for i in range(len(words)):
            password = words[i]
            self.chrome.find_element(*self.PASSWORD_INPUT).send_keys(password)
            actual = self.chrome.current_url
            expected = 'https://the-internet.herokuapp.com/secure'
            if actual == expected:
                print(f'The secret pasword is {password}.')
                break
            else:
                print('I couldn\'t find the password.')




