#!/usr/bin/python3


def main():
    from add_0 import add as adder
    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, adder(a, b)))

if (__name__ == '__main__'):
    main()
