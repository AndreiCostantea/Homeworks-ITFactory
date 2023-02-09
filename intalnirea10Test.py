from unittest import TestCase
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
from webdriver_manager.drivers import chrome
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

class CheckBoxTextTest(TestCase):
    CHECKBOXLINK = (By.LINK_TEXT, 'Checkboxes')
    HEADERCSS = (By.CSS_SELECTOR, 'h3')
    FIRSTCHECKBOXXPATH = (By.XPATH, '//input[@type="checkbox"][1]')
    def setUp(self):
        self.firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.firefox.get('https://the-internet.herokuapp.com/')
        self.firefox.maximize_window()
        self.firefox.find_element(*self.CHECKBOXLINK).click()    #=> steluta colecteaza toate elementele din tupla chechboxLink
        self.firefox.implicitly_wait(5)

    def tearDown(self):
        self.firefox.quit()

    def testCheckURL(self):
        actual = self.firefox.current_url
        expected = '/checkboxes'
        self.assertTrue(expected in actual, 'URL gresit')

    def testCheckHeader(self):
        actual = self.firefox.find_element(*self.HEADERCSS).text
        expected = 'Checkboxes'
        self.assertEqual(expected, actual, 'header gresit')

    def testSelectCheckBox1(self):
        box = self.firefox.find_element(*self.FIRSTCHECKBOXXPATH)
        box.click()
        self.assertTrue(box.is_selected(), 'box unchecked')