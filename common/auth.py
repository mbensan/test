# -*- coding: utf-8 -*-
'''
    Rutina común de login en la plataforma
'''
import sys
from selenium import webdriver
from config import config
import unittest


class ParamTestCase(unittest.TestCase):

    def __init__(self, methodName='testRun', driver=None, config={}, **kwargs):
        super(ParamTestCase, self).__init__(methodName)
        self.driver = driver
        self.config = config
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def table_sortable_columns(self, table_css_selector, col_names):
        '''
        Function: table_sortable_columns
        Summary: Comprueba que una tabla tenga columnas ordenables
        Attributes:
            @param (self):InsertHere
            @param (table_css_selector): string
            @param (col_names): [string]
        Returns: void
        '''
        def sort_dash_end(list, reverse=False):
            ''' Funcion de ordenamiento que siempre deja los guiones al final '''
            new_list = sorted([elem for elem in list if elem != '-'], reverse=reverse)
            slashs = [elem for elem in list if elem == '-']
            return new_list + slashs

        table = self.driver.find_element_by_css_selector(table_css_selector)
        t_headers = table.find_elements_by_css_selector('th')

        for i in range(len(t_headers)):
            if t_headers[i].text in col_names:
                # selecciona solo columnas que despliegan datos. Se clickea dos veces
                for j in xrange(2):
                    t_headers[i].click()
                    # se obtiene las celdas de la columna seleccionadda
                    rows = table.find_elements_by_xpath('.//tbody//tr/td[' + str(i + 1) + ']')
                    rows_values = [row.text for row in rows]

                    if 'sort-up' in t_headers[i].get_attribute('class'):
                        self.assertTrue(sort_dash_end(rows_values, reverse=True) == rows_values,
                                        'La lista %s no es igual a %s' %
                                        (sort_dash_end(rows_values, reverse=True), rows_values))

                    elif 'sort-down' in t_headers[i].get_attribute('class'):
                        self.assertTrue(sort_dash_end(rows_values) == rows_values,
                                        'La lista %s no es igual a %s' %
                                        (sort_dash_end(rows_values), rows_values))


def get_driver():
    try:
        driver = getattr(webdriver, config['driver'])()
    except AttributeError:
        print 'Driver %s no existe en selenium' % config['driver']
        sys.exit(0)

    driver.get(config['url'])
    assert 'Wivo' in driver.title

    return driver


def close_driver(driver):
    driver.close()
