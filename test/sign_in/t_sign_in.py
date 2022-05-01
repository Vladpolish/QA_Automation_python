# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import css_locators
import project_parameters


# import test.sign_in
# from test/sign_in import project_parameters
# import sys
# sys.path.insert(0, '')
# import test.sign_in.project_parameters
# from test.sign_in import project_parameters
# sys.path.insert(1, '/test/sign_in/')


class TestSignIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sign_in(self):
        driver = self.driver
        self.open_login_page(driver)
        self.sign_in(driver)

        # my_profile = driver.find_element(By.LINK_TEXT, 'My Profile')
        # my_profile.click()
        #
        # sign_out = driver.find_element(By.LINK_TEXT, 'Sign Out')
        # sign_out.click()


    def sign_in(self, driver):
        # Signin
        username = driver.find_element(By.CSS_SELECTOR, css_locators.username)
        username.click()

        username.send_keys(f'{project_parameters.email}')
        password = driver.find_element(By.CSS_SELECTOR, css_locators.password)
        password.click()

        password.send_keys(f'{project_parameters.password}')
        submit_button = driver.find_element(By.CSS_SELECTOR, css_locators.submit)
        submit_button.click()

        time.sleep(10)

    def open_login_page(self, driver):
        # Open login page
        driver.get(f'{project_parameters.app_url}')

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
