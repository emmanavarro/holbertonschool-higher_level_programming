#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) is 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) is 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for index in range(1, len(sys.argv)):
            print("{:d}: {}".format(index, sys.argv[index]))
