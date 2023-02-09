# Teme sesiunea 8
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep


# (1) site -> https://www.techlistic.com/p/selenium-practice-form.html

class PracticeForm():
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome = webdriver.Chrome()
    def __init__(self):
        self.chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
        self.chrome.maximize_window()

    def signUpForm(self):
        self.chrome.find_element(By.ID, 'ez-accept-all').click()
        sleep(1)
        self.chrome.find_element(By.NAME, 'firstname').send_keys('Andrei')
        sleep(1)
        self.chrome.find_element(By.NAME, 'lastname').send_keys('Costantea')
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, '#sex-0').click()
        sleep(1)
        self.chrome.find_element(By.ID, 'exp-3').click()
        sleep(1)
        self.chrome.find_element(By.ID, 'datepicker').send_keys('03.12.2022')
        sleep(1)
        self.chrome.find_element(By.ID, 'profession-1').click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, '#tool-2').click()
        sleep(1)
        self.chrome.find_element(By.ID, 'continents').send_keys('eu')
        sleep(1)
test = PracticeForm()
test.signUpForm()

# (2) site -> https://formy-project.herokuapp.com/

class Formy():
    chrome = webdriver.Chrome()

    def __init__(self):
        self.chrome.get('https://formy-project.herokuapp.com/')
        self.chrome.maximize_window()

    def Autocomp(self):
        self.chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
        sleep(1)
        self.chrome.find_element(By.ID, 'autocomplete').send_keys('garbau 3 cluj')
        sleep(1)
        self.chrome.find_element(By.CLASS_NAME, 'dismissButton').click()
        sleep(1)
        self.chrome.find_element(By.ID, 'street_number').send_keys('str. Garbau')
        sleep(1)
        self.chrome.find_element(By.ID, 'route').send_keys('nr. 3')
        sleep(1)
        self.chrome.find_element(By.ID, 'locality').send_keys('Cluj')
        sleep(1)
        self.chrome.find_element(By.ID, 'administrative_area_level_1').send_keys('--')
        sleep(1)
        self.chrome.find_element(By.ID, 'postal_code').send_keys('0000')
        sleep(1)
        self.chrome.find_element(By.ID, 'country').send_keys('Englezia')
        sleep(3)

    def checkBox(self):
        def checkBox(self):
            self.chrome.find_element(By.LINK_TEXT, 'Checkbox').click()
            sleep(1)
            self.chrome.find_element(By.ID, 'checkbox-1').click()
            sleep(2)
            self.chrome.find_element(By.ID, 'checkbox-2').click()
            sleep(2)
            self.chrome.find_element(By.ID, 'checkbox-3').click()
            sleep(2)


test2 = Formy()
#test2.Autocomp()
test2.checkBox()

