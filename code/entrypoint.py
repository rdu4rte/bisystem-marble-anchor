from argparse import ArgumentParser, Namespace
from modules.users import UsersOperations
from modules.sales import SalesOperations
from config.logger import main_logger
from modules.items import ItemsOperations
from connectors.mongodb import mongo_connection


def bootstrap():
    # logger
    main_logger(args)

    # mongodb connector
    db_connection = mongo_connection()

    # modules mapper
    map_modules: dict = {
        "items": ItemsOperations(
            db_connection=db_connection,
            channel=args.channel,
            action=args.action,
        ),
        "users": UsersOperations(
            db_connection=db_connection,
            channel=args.channel,
            action=args.action,
        ),
        "sales": SalesOperations(
            db_connection=db_connection,
            channel=args.channel,
            action=args.action,
        ),
    }

    if args.module == "bootstrap":
        return print("[Bootstrap] RUN_CMD")

    return map_modules[args.module].perform()


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(prog="main")
    parser.add_argument(
        "-m", "--module", help="items, sales, users", type=str
    )
    parser.add_argument("-c", "--channel", help="0, 1, 2", type=int)
    parser.add_argument("-a", "--action", help="selected action", type=str)

    args: Namespace = parser.parse_args()

bootstrap()
