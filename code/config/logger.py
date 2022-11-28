import logging as logger
import datetime

logger.basicConfig(filename="logs/log_history.log", level=logger.INFO)


def main_logger(args):
    logger.info(
        "[Bootstrap] module: {}, action: {}, channel: {}, time: {}".format(
            args.module, args.action, args.channel, datetime.datetime.now()
        )
    )
