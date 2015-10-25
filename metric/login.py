# -*- coding: utf-8 -*-
'''
    Pruebas de pantalla: Metricas de tiendas
'''
import unittest
from common.auth import ParamTestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Login(ParamTestCase):
    def test_login(self):

        self.assertTrue('Wivo' in self.driver.title)
        username = self.driver.find_element_by_id("username-f")
        password = self.driver.find_element_by_id("password-f")

        username.send_keys(self.config['user']['username'])
        password.send_keys(self.config['user']['password'])
        password.submit()

        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.presence_of_element_located((By.ID, 'shops')))


if __name__ == '__main__':
    unittest.main()
