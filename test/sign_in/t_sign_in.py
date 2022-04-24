# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
# import test.sign_in

# from test/sign_in import project_parameters
# import sys
# sys.path.insert(0, '')
# import test.sign_in.project_parameters
# from test.sign_in import project_parameters

# import sys
import project_parameters

# sys.path.insert(1, '/test/sign_in/')


class TestSignIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sign_in(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1366,610 | ]]

        driver.get(f'{project_parameters.app_url}')

        # username = driver.find_element_by_id("username")
        username = driver.find_element(By.CSS_SELECTOR, "#username")
        username.click()
        username.send_keys(f'{project_parameters.email}')

        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.click()
        password.send_keys(f'{project_parameters.password}')

        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

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
