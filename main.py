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
    while (42):
        temp = input()
        if temp == "STOP":
            break
        try:
            temp = float(temp)
        except ValueError:
            stderr.write("INVALID TEMPERATURE")
            continue
        temperatures.append(temp)
        choose_display(temperatures, period)
    print("Global tendency switched " + str(get_switch.count) + " times")
    print("5 weirdest values are " + str(get_aberrations()))


def main():
    """main."""
    if len(argv) != 2 or argv[1].isnumeric() == False:
        print("INVALID USAGE")
        helper()
        exit (84)
    elif argv[1] == "-h":
        helper()
    else:
        groundhog()
        return (0)

if __name__ == "__main__":
    main()
