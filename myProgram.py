# Title: My program - Adds or multiply two arguments
# Author: Miguel García 
# Based on https://docs.python.org/3/howto/argparse.html by Tshepang Lekhonkhobe

import argparse

parser = argparse.ArgumentParser(description=
"****************************************************************************\n"
"This code will take 2 number and add them or multiply them (Default=ADD)\n"
"****************************************************************************")
group = parser.add_mutually_exclusive_group()
parser.add_argument("x", type=int, help="First number")
parser.add_argument("y", type=int, help="Second number")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-s", "--sum", action="store_true", default=True)
parser.add_argument("-m", "--multiply", action="store_true")
args = parser.parse_args()

if args.sum:
    answer = args.x + args.y
    if args.verbose:
        print("{} summed with {} equals {}".format(args.x, args.y, answer))
    else:
        print(answer)
elif args.multiply:
    answer = args.x * args.y
    if args.verbose:
        print("{} multiplied by {} equals {}".format(args.x, args.y, answer))
    else:
        print(answer)