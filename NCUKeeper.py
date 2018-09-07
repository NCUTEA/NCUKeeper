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
    INTERVAL = 3

    while True:
        count = 0
        flag = False
        while count < 3:
            try:
                isOnline = ncuwlan.is_online_by_baidu()
                logger.debug("Online:" + str(isOnline))
                if isOnline:
                    flag = True
                    break
            except:
                try:
                    isNCU = ncuwlan.is_online_by_ncu()
                    if isNCU:
                        logger.info("Trying to connect...\n")
                        ncuwlan.login()
                        logger.info("Status:" + str(ncuwlan.status()))
                except:
                    pass
            finally:
                time.sleep(INTERVAL)
                count += 1
        if not flag:
            logger.info("失败多次，将休眠一段时间")
            time.sleep(10)

