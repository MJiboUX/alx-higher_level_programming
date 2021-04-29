#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arguments = len(sys.argv) - 1
    if len(sys.argv) is 1:
        print('0 arguments.')
    else:
        print ('{} arguments'.format(arguments))
        print ('{}'.format(str(sys.argv)))
