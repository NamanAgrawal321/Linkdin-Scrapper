import logging
from logging.handlers import RotatingFileHandler

def get_logger(fileName, log_level=logging.DEBUG):
    """Using get_logger to track and store the process and exicutions

    Args:
        file_log (_type_): __file_name__
        log_level (_type_, optional): _description_. Defaults to logging.INFO.
    """
    # create logger
    logger = logging.getLogger(fileName[:fileName.index('.')])
    logger.setLevel(log_level)

    # create handler
    rf_handler= RotatingFileHandler(fileName,"a",40000000,3)
    rf_handler.setLevel(log_level)

    # create formatter
    format = "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(thread)d - %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(format, datefmt)
    rf_handler.setFormatter(formatter)
    logger.addHandler(rf_handler)
    return logger

