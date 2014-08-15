import logging
from logging.handlers import RotatingFileHandler

from touchandgo.settings import DEBUG, TMP_DIR


def log_set_up(verbose):

    logfile = "%s/touchandgo.log" % (TMP_DIR)
    handler = RotatingFileHandler(logfile, maxBytes=1e6, backupCount=10)
    formatter = logging.Formatter("%(asctime)s  %(name)-22s  "
                                  "%(levelname)-8s %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger('touchandgo')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    if DEBUG:
        logger.setLevel(logging.DEBUG)
    if verbose:
        handler = logging.StreamHandler()
        logger.addHandler(handler)
        handler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
