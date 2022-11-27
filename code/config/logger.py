import logging as logger
import datetime

logger.basicConfig(filename='logs/log_history.log', level=logger.INFO)


def main_logger(args):
  logger.info(
      f'[Bootstrap] module: {args.module}, action: {args.action}, channel: {args.channel}, time: {datetime.datetime.now()}')
