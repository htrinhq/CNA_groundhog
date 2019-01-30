#Display functions for GroundHog

from stats import *

def display(temperatures, period):
    #Display Stats about Temperatures
    r = tempIncreaseAvg(temperatures, period)
    g = relativeTempEv(temperatures, period)
    s = standardDeviation(temperatures, period)
    if getSwitch(r) == True:
        print("g=" + "{0:.2f}".format(g), "r=" + "{0:.0f}".format(r) + "%",
              "s=" + "{0:.2f}".format(s), "a switch occurs", sep="\t\t")
    else:
        print("g=" + "{0:.2f}".format(g), "r=" + "{0:.0f}".format(r) + "%",
              "s=" + "{0:.2f}".format(s), sep="\t\t")


def chooseDisplay(temperatures, period):
    #Select correct output to display
    if len(temperatures) < period:
        print("g=nan", "r=nan%", "s=nan", sep="\t\t")
    elif len(temperatures) == period:
        print("g=nan", "r=nan%", "s=" +
              "{0:.2f}".format(standardDeviation(temperatures, period)), sep="\t\t")
    else:
        display(temperatures, period)

def helper():
    #Display Help for launch
    print("SYNOPSIS\n\t./groundhog period\n")
    print("DESCRIPTION\n\tperiod\tthe number of days defining a period")
