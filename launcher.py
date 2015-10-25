# -*- coding: utf-8 -*-
'''
    lanzador de tests de . Colocar todos los test en el main
'''
from common.util import make_suite
from common import auth
from common.config import config as config_dict

from metric.login import Login
from goal.user_goals import UsersGoals
from metric.user_stores import UserStores
from metric.store_view import make_store_view_suite

def main():
    driver = auth.get_driver()

    make_suite(Login, driver, config_dict)
    make_suite(UserStores, driver, config_dict,
               config_dict['url'] + '/#graphs/shops')
    make_suite(UsersGoals, driver, config_dict,
               config_dict['url'] + '/#goals/shops')

    make_store_view_suite(driver, config_dict)
    auth.close_driver(driver)
    # sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    main()
