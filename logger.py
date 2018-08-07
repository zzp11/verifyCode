import logging
import sys
from functools import partial

logger = logging.getLogger('verifycode')
logger.setLevel(level=logging.DEBUG)

debug_handler = logging.StreamHandler(sys.stdout)
debug_handler.setLevel(level=logging.DEBUG)
logger.addHandler(debug_handler)

info_handler = logging.FileHandler('./logs/info.log')
info_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s %(filename)s %(lineno)s: %(message)s')
info_handler.setFormatter(formatter)
logger.addHandler(info_handler)

error_handler = logging.FileHandler('./logs/error.log')
error_handler.setLevel(level=logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s %(filename)s %(lineno)s: %(message)s')
error_handler.setFormatter(formatter)
logger.addHandler(error_handler)

#logger.error = partial(logger.error, exc_info=True)

if __name__ == '__main__':
    logger.info('log info')
    logger.debug('log debug')
    logger.warn('log warning')
    logger.error('log error')
    logger.fatal('log fatal')
    try:
        a = 1 / 0
    except Exception as e:
        logger.error('error', exc_info=True)



