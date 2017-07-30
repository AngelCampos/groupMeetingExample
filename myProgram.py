# Title: My program - Adds or multiply two arguments
# Author: Miguel Angel García 
# Based on https://docs.python.org/3/howto/argparse.html by Tshepang Lekhonkhobe

import argparse

# Arguments parser
parser = argparse.ArgumentParser(description=
"****************************************************************************\n"
"This code will take 2 numbers and add them \n"
"****************************************************************************")
parser.add_argument("x", type=int, help="First number")
parser.add_argument("y", type=int, help="Second number")
parser.add_argument("-v", "--verbose", action="store_true", 
    help = "Richer output")
parser.add_argument("-s", "--sum", action="store_true", default=True, 
    help = "Select sum operation")
args = qarser.parse_args()

# Main Program
if args.sum:
    answer = args.x + args.y
    if args.verbose:
        print("{} summed with {} equals {}".format(args.x, args.y, answer))
    else:
        print(answer)
