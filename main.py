#!/usr/bin/env python3

#GroundHog main file.
from sys import *
from math import *
from statistics import mean, pstdev
from stats import *
from display import *

def groundhog():
    """main loop for groundhog program."""
    period = int(argv[1])
    temperatures = []
    aberrations = []
    if period == 0:
        print("INVALID USAGE")
        helper()
        exit(84)
    while (42):
        try:
            temp = input()
        except EOFError:
            return
        if temp == "STOP":
            break
        try:
            temp = float(temp)
        except ValueError:
            stderr.write("INVALID TEMPERATURE\n")
            continue
        temperatures.append(temp)
        choose_display(temperatures, period)
    print("Global tendency switched " + str(get_switch.count) + " times")
    aberrations = get_aberrations()
    if len(aberrations) == 0:
        print('No weird values')
    else:
        print(str(len(aberrations)) + " weirdest values are "
        + str(aberrations))


def main():
    """main."""
    if len(argv) == 2 and argv[1] == "-h":
        helper()
        exit (0)
    elif len(argv) != 2 or argv[1].isnumeric() == False:
        print("INVALID USAGE")
        helper()
        exit (84)
    else:
        groundhog()
        return (0)

if __name__ == "__main__":
    main()
