# -*- coding: utf-8 -*-
'''
    Pruebas de pantalla: Metricas de tiendas
'''
import unittest
from common.auth import ParamTestCase
from common.util import make_suite
from store_view import StoreView


class UserStores(ParamTestCase):
    table_css_selector = '.shops'

    def test_sort_table(self):

        self.table_sortable_columns('.shops', [u'NOMBRE', u'VENTAS', u'VISITAS',
                                               u'CONVERSIÓN', u'TICKET PROMEDIO'])

    def test_units_table(self):
        units_dict = {
            'NOMBRES': {
            },
            'VENTAS': {
                'prefix': '$'
            },
            'VISITAS': {
            },
            'CONVERSIÓN': {
                'suffix': '%'
            },
            'TICKET PROMEDIO': {
                'prefix': '$'
            }
        }

        table = self.driver.find_element_by_css_selector(self.table_css_selector)

        t_headers = table.find_elements_by_css_selector('th')
        for i in range(len(t_headers)):
            # selecciona solo columnas que despliegan datos. Se clickea dos veces
            header = t_headers[i].text
            if header in units_dict.keys():

                rows = table.find_elements_by_xpath('.//tbody//tr/td[' + str(i + 1) + ']')
                for row in rows:
                    self.assertTrue(row.text != '', 'El texto %s es vacio' % row.text)
                    if row.text == '-':
                        continue

                    if 'prefix' in units_dict[header].keys():
                        self.assertTrue(row.text.startswith(units_dict[header]['prefix']),
                                        'El campo de %s %s debe tener prefijo %s' %
                                        (header, row.text, units_dict[header]['prefix']))

                    if 'suffix' in units_dict[header].keys():
                        self.assertTrue(row.text.endswith(units_dict[header]['suffix']),
                                        'El campo de %s %s debe tener sufijo %s' %
                                        (header, row.text, units_dict[header]['suffix']))
if __name__ == '__main__':
    unittest.main()
