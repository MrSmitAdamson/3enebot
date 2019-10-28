import logging
import logging.handlers
logger = None
 
def set_logging():
    global logger
    logger = logging.getLogger("main")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    file_logger = logging.handlers.RotatingFileHandler("log.txt", maxBytes=10000000, backupCount=5)
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(formatter)
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.DEBUG)
    console_logger.setFormatter(formatter)
    logger.addHandler(file_logger)
    logger.addHandler(console_logger)
 
set_logging()

logger = logger.info
#logger.info('INFO?')
