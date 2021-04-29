#!/usr/bin/python3
import sys
def main(*argv):
    arguments = len(sys.argv) - 1
    sum = 0
    if arguments == 1:
        print("{:d} argument:".format(arguments))
    elif arguments == 0:
        print("{:d} argument".format(arguments))
    else:
        print("{:d} arguments".format(arguments))
    for args in sys.argv:
            if args != sys.argv[0]:
                sum = sum + int(args)
    print(sum)

if __name__ == "__main__":
    main()
