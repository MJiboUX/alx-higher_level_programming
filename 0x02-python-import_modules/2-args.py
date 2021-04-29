#!/usr/bin/python3
import sys
def main(*argv):
    arguments = len(sys.argv) - 1
    position = 0
    if arguments == 1:
        print("{:d} argument:".format(arguments))
    elif arguments == 0:
        print("{:d} argument".format(arguments))
    else:
        print("{:d} arguments".format(arguments))
    for args in sys.argv:
        if (position != 0):
            print("{}: {}".format(position, args))
        position += 1
if __name__ == "__main__":
    main()
