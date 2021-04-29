#!/usr/bin/python3
import sys
def main(*argv)
    arguments = len(sys.argv) - 1
    position = 0
    if arguments == 1:
        print("{:d} argument:".format(arguments))
    elif arguments == 0:
        print("{:d} argument".format(arguments))
    else:
        print("{:d} arguments".format(arguments))
    for texts in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, texts))
        i += 1
if __name__ == "__main__":
    main()
