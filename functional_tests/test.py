from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import unittest

import time


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class dublinBus(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def test_joureny_planner(self):
        """Testing the functionality of the journey planner"""
        driver = self.driver
        driver.get("http://localhost:8080/login/")        
        time.sleep(5)
        dest_input = driver.find_element(By.ID, "enterYourDestionation")
        dest_input.send_keys('Dawson street, Dublin')
        time.sleep(5)
        dest_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        dest_input.send_keys(Keys.ENTER)
        time.sleep(2)
        press_marker = driver.find_element(By.ID, "endMarkerBtn")
        press_marker.click()
        time.sleep(2)
        submit_button = driver.find_element(By.ID, "submitButton")
        submit_button.click()
        time.sleep(5)

    def test_login(self):
        """Testing invalid user for log in section"""

        driver = self.driver
        driver.get("http://localhost:8080/login/")
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys('gus')
        time.sleep(1)
        pass_input = driver.find_element(By.ID, "password")
        pass_input.send_keys('password')
        time.sleep(1)
        login_button = driver.find_element(By.NAME, 'login_Button')
        login_button.click()
        time.sleep(2)
        # error_message = driver.find_element(By.ID, 'errorMsg')
        self.assertIn('Wrong', driver.page_source)

    def test_register_already_exists(self):
        """Testing register page when the user already exists"""

        driver = self.driver
        driver.get("http://localhost:8080/register/")
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys('gus')
        time.sleep(1)
        pass_input = driver.find_element(By.ID, "password")
        pass_input.send_keys('password')
        time.sleep(1)
        pass_confrim = driver.find_element(By.ID, "password_confirm")
        pass_confrim.send_keys('password')
        time.sleep(1)
        singin_button = driver.find_element(By.ID, 'sigupBtn')
        singin_button.click()
        time.sleep(3)
        self.assertIn('already', driver.page_source)


    def test_register_passwords(self):
        """Testing sign up of new user when passwords don't match"""

        driver = self.driver
        driver.get("http://localhost:8080/register/")
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys('newUser')
        time.sleep(1)
        pass_input = driver.find_element(By.ID, "password")
        pass_input.send_keys('password')
        time.sleep(1)
        pass_confrim = driver.find_element(By.ID, "password_confirm")
        pass_confrim.send_keys('password1')
        time.sleep(1)
        singin_button = driver.find_element(By.ID, 'sigupBtn')
        singin_button.click()
        time.sleep(3)
        self.assertIn('do not match', driver.page_source)

    def test_register_correct(self):
        """Testing sign up of new user"""

        driver = self.driver
        driver.get("http://localhost:8080/register/")
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys('newUser123')
        time.sleep(1)
        pass_input = driver.find_element(By.ID, "password")
        pass_input.send_keys('password123')
        time.sleep(1)
        pass_confrim = driver.find_element(By.ID, "password_confirm")
        pass_confrim.send_keys('password123')
        time.sleep(1)
        singin_button = driver.find_element(By.ID, 'sigupBtn')
        singin_button.click()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()