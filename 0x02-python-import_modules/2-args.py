#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arguments = len(sys.argv) - 1
    position = 1
    if len(sys.argv) is 1:
        print('0 arguments.')
    else:
        while (arguments >= position):
            print('{:d}: {:s}'.format(position, sys.argv[position]))
