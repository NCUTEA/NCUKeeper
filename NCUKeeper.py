# -*- coding: utf-8 -*-
import logging
import sys
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
    INTERVAL = 10

    while True:
        isOnline = ncuwlan.is_online_by_baidu()
        logger.debug("Online:" + str(isOnline))
        if isOnline:    # 在线
            pass
        else:
            isNCU = ncuwlan.is_online_by_ncu()
            if isNCU:   # 离线 是NCU
                logger.info("Trying to connect...\n")
                ncuwlan.login()
                logger.info("Status:" + str(ncuwlan.status()))
            else:       # 不是NCU
                logger.error("似乎连接网络失败")
                sys.exit(-1)
        time.sleep(INTERVAL)



