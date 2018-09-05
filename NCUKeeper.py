# -*- coding: utf-8 -*-
import logging
import time

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
    INTERVAL = 1

    while True:
        time.sleep(INTERVAL)
        isOnline = ncuwlan.is_online_by_baidu()
        logger.debug("Online:" + str(isOnline))
        if isOnline:
            pass
        else:
            logger.info("Connect to Baidu.com Failed!\n")
            ncuwlan.login()
            logger.info("Status:" + ncuwlan.status())
