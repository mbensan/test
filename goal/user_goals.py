# -*- coding: utf-8 -*-
'''
    Pruebas de pantalla: Metas de tiendas
'''
from common.auth import ParamTestCase


class UsersGoals(ParamTestCase):

    def test_sort_table(self):
        self.table_sortable_columns('.goals-table', [u'LOCAL', u'AVANCE', u'META',
                                                     u'TIEMPO RESTANTE'])
