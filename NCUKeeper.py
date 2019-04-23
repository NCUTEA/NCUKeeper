# -*- coding: utf-8 -*-
import logging
import sys
import time

from NCUWLAN import NCUWLAN
from NCUWLAN import is_online_by_baidu

if __name__ == '__main__':

    logger = logging.getLogger('root')
    log_level = logging.DEBUG
    log_format = '[%(asctime)s][%(filename)s][L%(lineno)d][%(levelname)s] %(message)s'
    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    # TODO: cli: command level
    ncuwlan = NCUWLAN()
    INTERVAL = 20
    while True:
        isOnline = is_online_by_baidu()
        logger.info("外网连通性:" + str(isOnline))
        if isOnline:
            pass
        else:
            isNCU = ncuwlan.is_online_by_ncu()
            logger.debug("NCUWLAN连通性:" + str(isOnline))
            if isNCU:
                logger.info("尝试重新登录")
                ncuwlan.login()
                logger.info("NCUWLAN状态:" + str(ncuwlan.status()))
            else:
                logger.error("无法连接到NCUWLAN...")

        time.sleep(INTERVAL)
