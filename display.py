#Display functions for GroundHog.

from stats import *

def display(temperatures: [float], period: int):
    """Display Stats about Temperatures."""
    r = temp_increase_avg(temperatures, period)
    g = relative_temp_ev(temperatures, period)
    s = standard_deviation(temperatures, period)
    if get_switch(r) == True:
        print("g=" + "{0:.2f}".format(g), "r=" + "{0:.0f}".format(r) + "%",
              "s=" + "{0:.2f}".format(s), "a switch occurs", sep="\t")
    else:
        print("g=" + "{0:.2f}".format(g), "r=" + "{0:.0f}".format(r) + "%",
              "s=" + "{0:.2f}".format(s), sep="\t")


def choose_display(temperatures: [float], period: int):
    """Select correct output to display."""
    if len(temperatures) < period:
        print("g=nan", "r=nan%", "s=nan", sep="\t")
    elif len(temperatures) == period:
        print("g=nan", "r=nan%", "s=" +
              "{0:.2f}".format(standard_deviation(temperatures, period)), 
              sep="\t")
    else:
        display(temperatures, period)

def helper():
    """Display Help for launch."""
    print("SYNOPSIS\n\t./groundhog period\n")
    print("DESCRIPTION\n\tperiod\tthe number of days defining a period")
