# CLI (command-line interface)
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("name", type=str)
# args.add_argument("--age", type=int, nargs='?', default=0)
# args.add_argument("--job", type=str, nargs='?', default='')

args = vars(args.parse_args())
print(args)

# name = args['name']
# age = args['age'] * 2
#
# print(f"Hello {name}! ]Age: {age}")