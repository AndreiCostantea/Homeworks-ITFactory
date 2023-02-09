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

class Test(TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()
        self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()


    def tearDown(self):
        self.chrome.quit()

    def test1_URL(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'URL incorect')

    def test2_title(self):
        titlu = self.chrome.find_element(By.CSS_SELECTOR, 'h2')
        actual = titlu.text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Titlu incorect')

    def test3_element(self):
        text = self.chrome.find_element(By.XPATH, '//h2')
        actual = text.text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'text incorect')

    def test4_login(self):
        buton = self.chrome.find_element(By.CLASS_NAME, 'radius')
        actual = buton.text
        expected = 'Login'
        self.assertEqual(expected, actual, 'Buton nu exista')

    def test5_linkElementalS(self):
        url = self.chrome.find_element(By.LINK_TEXT, 'Elemental Selenium').get_attribute('href')
        actual = url
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'link gresit')

    def test6_eroare(self):
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        eroare = self.chrome.find_element(By.CSS_SELECTOR, '#flash')
        actual = eroare.text
        expected = 'Your username is invalid!\n×'
        self.assertEqual(expected, actual, 'eroarea nu apare')

    def test7_user_pass_invalid(self):
        self.chrome.find_element(By.ID, 'username').send_keys('Andrei')
        self.chrome.find_element(By.ID, 'password').send_keys('Raul')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        eroare = self.chrome.find_element(By.CSS_SELECTOR, '#flash')
        actual = eroare.text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'error message text is incorrect')

    def test8_dispare_eroare(self):
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        self.chrome.find_element(By.XPATH, '//a[normalize-space()="×"]').click()
        sleep(5)
        try:
            eroare = self.chrome.find_element(By.XPATH, '(//div[@id="flash"])[1]') # xpath eroare
        except NoSuchElementException:
            print('Elementul dispare')

    def test9_textAsteptat(self):
        label1 = self.chrome.find_element(By.XPATH, '//label[normalize-space()="Username"]')
        label2 = self.chrome.find_element(By.XPATH, '//label[normalize-space()="Password"]')
        lista = [label1.text, label2.text]
        expected1 = 'Username'
        expected2 = 'Password'
        self.assertEqual(expected1, lista[0], 'nu apare username')
        self.assertEqual(expected2, lista[1], 'nu apare password')

    def test10_user_pass_valide(self):
        self.chrome.find_element(By.ID, 'username').click()
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').click()
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        expected = '/secure'
        actual = self.chrome.current_url
        self.assertTrue(expected in actual, 'URL gresit')
        WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located((By.ID, 'flash')))
        display = self.chrome.find_element(By.ID, 'flash')
        displayActual = display.is_displayed()
        print(displayActual)
        expected = True
        self.assertTrue(displayActual, 'elementul nu este displayed')

    def test11_logut(self):
        self.chrome.find_element(By.ID, 'username').click()
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').click()
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.CLASS_NAME, 'radius').click()
        self.chrome.find_element(By.XPATH, '//a[@class="button secondary radius"]').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'URL gresit')

# teme - optionale

    def test12_bruteForce_passHacking(self):
        para = self.chrome.find_element(By.CLASS_NAME, 'subheader').text
        textSplited = para.split(' ')

        for x in textSplited:
            if x != 'SuperSecretPassword!':
                self.chrome.find_element(By.ID, 'username').click()
                self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
                self.chrome.find_element(By.ID, 'password').click()
                self.chrome.find_element(By.ID, 'password').send_keys(f'{x}')
                print(f'{x} nu este parola. Nu am reusit sa gasesc parola. Mai incercam')
                self.chrome.find_element(By.CLASS_NAME, 'radius').click()
            elif x == 'SuperSecretPassword!':
                self.chrome.find_element(By.ID, 'username').click()
                self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
                self.chrome.find_element(By.ID, 'password').click()
                self.chrome.find_element(By.ID, 'password').send_keys(f'{x}')
                print(f'Parola este {x}')
                self.chrome.find_element(By.CLASS_NAME, 'radius').click()
                sleep(2)
            if '/secure' in self.chrome.current_url:
                break