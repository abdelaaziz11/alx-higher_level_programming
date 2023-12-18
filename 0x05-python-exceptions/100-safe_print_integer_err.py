#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        int_val = int(value)
        print("{:d}".format(int_val))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
