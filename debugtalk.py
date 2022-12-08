import logging
import time
import random
from typing import List
import os
from loguru import logger
import toml
from decimal import *


# commented out function will be filtered
# def get_headers():
#     return {"User-Agent": "hrp"}


# def get_user_agent():
#     return "hrp/funppy"
#
#
# def sleep(n_secs):
#     time.sleep(n_secs)
#
#
# def sum(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# def sum_ints(*args: List[int]) -> int:
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# def sum_two_int(a: int, b: int) -> int:
#     return a + b
#
#

def sum_usable_inventory(a, b):
    return int(a)-int(b)

def sum_occupy_inventory(a,b):
    return int(a)+int(b)

def convert_int(a):
    return int(a)
#
#
# def sum_strings(*args: List[str]) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# def concatenate(*args: List[str]) -> str:
#     result = ""
#     for arg in args:
#         result += str(arg)
#     return result
#
#
# def setup_hook_example(name):
#     logger.info("setup_hook_example")
#     return f"setup_hook_example: {name}"
#
#
# def setup_hook_sql(sql):
#     logger.warning("setup_hook_sql")
#     logger.warning(f'sql is : {sql}')
#     db_host = os.environ.get("db_host")
#     db_port = os.environ.get("db_port")
#     db_user = os.environ.get("db_user")
#     db_pwd = os.environ.get("db_pwd")
#     db_name = os.environ.get("db_name")
#     db_uri = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'
#     logger.debug(db_uri)
#     db = DBEngine(db_uri)
#     db.delete(sql)
#     return f"teardown_hook_example: {sql}"
#
#
# def teardown_hook_example(name):
#     logger.debug("teardown_hook_example")
#     return f"teardown_hook_example: {name}"
#
#
# def teardown_hook_sql(sql):
#     logger.debug("teardown_hook_sql")
#     logging.debug(f'sql is : {sql}')
#     db_host = os.environ.get("db_host")
#     db_port = os.environ.get("db_port")
#     db_user = os.environ.get("db_user")
#     db_pwd = os.environ.get("db_pwd")
#     db_name = os.environ.get("db_name")
#     db_uri = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'
#     logging.warning(db_uri)
#     db = DBEngine(db_uri)
#     db.delete(sql)
#     return f"teardown_hook_example: {sql}"
#
#
# def get_timestamp():
#     return str(int(time.time() * 1000))
#
#
# def get_random_number(min, max):
#     """
#     Return random integer in range [min, max], including both end points.
#     """
#     rm = random.randint(int(min), int(max))
#     return rm

def query_id(resp):
    '''获取订单'''
    with open(".env", "a", encoding="utf-8") as f:
        f.write('\n'+"id={0}".format(resp))
    return resp

def convert_dict(order_id):
    return [order_id]