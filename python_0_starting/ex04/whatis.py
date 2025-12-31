# Allowed functions : sys or any other library that allows to receive the args

import sys as s

argc = len(s.argv)

if argc > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(0)
if argc == 1:
    # print()
    sys.exit(0)

number = s.argv
try:
    number = int(number[1])
    if (number >= 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")