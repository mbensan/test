# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_cond


def make_suite(testcase_class, driver, config, init_url=None, **kwargs):
    '''
        Para construir un TestCase con argumentos personalizados
    '''
    testloader = unittest.TestLoader()
    testnames = testloader.getTestCaseNames(testcase_class)
    suite = unittest.TestSuite()
    for name in testnames:
        suite.addTest(testcase_class(name, driver=driver, config=config, **kwargs))

    if init_url:
        wait_for_url(driver, init_url)

    unittest.TextTestRunner(verbosity=2).run(suite)


def wait_for_url(driver, init_url):
    print init_url
    driver.get(init_url)

    try:
        WebDriverWait(driver, 10).until_not(
            e_cond.presence_of_element_located((By.CLASS_NAME, 'loading')))
    except TimeoutException:
        print "Mas de 10 segundos en cargar la URL: %s" % init_url


def set_calendar_last_3_days(driver):
    driver.find_element_by_css_selector('div.range').click()
    driver.find_element_by_css_selector('li#ui-id-2').click()


def set_calendar_last_30_days(driver):
    driver.find_element_by_css_selector('div.range').click()
    driver.find_element_by_css_selector('li#ui-id-4').click()