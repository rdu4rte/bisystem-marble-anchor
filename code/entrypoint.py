from argparse import ArgumentParser, Namespace


def bootstrap():
  print('hello from the other world')
  return {}


if __name__ == '__main__':
  parser: ArgumentParser = ArgumentParser(prog='main')
  parser.add_argument('-m', '--module', help='items, sales, users', type=str)
  parser.add_argument('-c', '--channel', help='0, 1, 2', type=int)
  parser.add_argument('-a', '--action', help='selected action', type=str)

  args: Namespace = parser.parse_args()

bootstrap()
