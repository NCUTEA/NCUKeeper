# -*- coding: utf-8 -*-
import logging
import time
from requests import exceptions

from NCUWLAN import NCUWLAN

if __name__ == '__main__':

    logger = logging.getLogger('root')
    log_level = logging.INFO
    log_format = '[%(asctime)s][%(filename)s][L%(lineno)d][%(levelname)s] %(message)s'
    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    # TODO: cli: command level
    ncuwlan = NCUWLAN()
    INTERVAL = 10

    while True:
        try:
            isOnline = ncuwlan.is_online_by_baidu()
            logger.debug("Online:" + str(isOnline))
            if isOnline:
                logger.debug("Connect to Baidu.com Succeed\n")
                pass
        except exceptions.ConnectionError:
            logger.error("您似乎未曾连接到网络...")
            break
        except exceptions.ConnectTimeout:
            logger.info("Connect to Baidu.com Failed!\n")
            try:
                ncuwlan.login()
                logger.info("Status:" + str(ncuwlan.status()))
            except IOError:
                logger.info("The interval is too short!")
                time.sleep(INTERVAL)
                ncuwlan.login()
        finally:
            time.sleep(INTERVAL)

