import logging
import time
import random
from typing import List
from httprunner.database.engine import DBEngine
import os
from loguru import logger
import toml

def t(sql):
    logger.debug("teardown_hook_sql")
    logging.debug(f'sql is : {sql}')
    db_host = os.environ.get("db_host")
    db_port = os.environ.get("db_port")
    db_user = os.environ.get("db_user")
    db_pwd = os.environ.get("db_pwd")
    db_name = os.environ.get("db_name")
    db_uri = f'mysql+pymysql://{"asura"}:{"asura"}@{"test.mysql8.ruigushop.com"}:{3306}/{"asura_wms_005"}?charset=utf8mb4'
    logging.warning(db_uri)
    db = DBEngine(db_uri)
    a = db.fetchone(sql)
    print(a["pass_status"])

if __name__ == '__main__':
    t("select * from asura_wms_005.out_plan where id = 81261020462477313;")