import logging as logger
import datetime

logger.basicConfig(filename="logs/log_history.log", level=logger.INFO)


def main_logger(args):
    logger.info(
        "[Bootstrap] module: {}, action: {}, time: {}".format(
            args.module, args.action, datetime.datetime.now()
        )
    )
