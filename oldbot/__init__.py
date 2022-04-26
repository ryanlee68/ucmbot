# inspired by https://github.com/Ahsoka/clovis/blob/main/clovis/__init__.py

import argparse

parser = argparse.ArgumentParser(description='Use this to set bot settings.')
parser.add_argument('-nt', '--not-testing', action='store_false', dest='testing')
config = parser.parse_args()