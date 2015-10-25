# -*- coding: utf-8 -*-
'''
    Pruebas de pantalla: Metricas de tiendas
'''
import unittest
from common.auth import ParamTestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.util import *


def make_store_view_suite(driver, config):
    wait_for_url(driver, config['url'] + '/#graphs/shops')
    store_trs = driver.find_elements_by_css_selector('tr[id^="shop-"]')
    ids = [int(store_tr.get_attribute('data-id')) for store_tr in store_trs]
    for store_id in ids:
        url = config['url'] + '/graphs/shop%i' % store_id
        make_suite(StoreView, driver, config, url, id=store_id)


class StoreView(ParamTestCase):
    def test_hourly_resolution(self):
        set_calendar_last_3_days(self.driver)

    def test_header(self):
        headers = self.driver.find_elements_by_css_selector('div#overview div span')
        footers = self.driver.find_elements_by_css_selector('span.value')
        self.assertEqual(len(headers), len(footers))
        for i in range(len(footers)):
            self.assertEqual(headers[i].text, footers[i].text)

    def test_header_clicks(self):
        overview = self.driver.find_element_by_id('overview')
        old_pos = -1
        page = self.driver.page
        for el in overview.find_elements_by_tag_name('div'):
            el.click()
            pos = driver.execute_script('return window.scrollY')
            self.assertNotEqual(pos, old_pos)
            old_pos = pos


if __name__ == '__main__':
    unittest.main()
