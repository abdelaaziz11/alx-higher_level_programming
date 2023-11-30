#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{:d} arguments.".format(n))
    else:
        if n == 1:
            print("{:d} argument:".format(n))
        else:
            print("{:d} arguments:".format(n))
        i = 1
        while i <= n:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
