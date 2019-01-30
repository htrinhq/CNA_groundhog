#Stats functions for GroundHog

from statistics import mean
from statistics import pstdev

def addToList(temp, old, diff):
    #Check value to append to the diff list
    if temp <= old:
        diff.append(0)
    else:
        diff.append(temp - old)


def relativeTempEv(temperatures, period):
    #Get the Relative Temperature Evolution
    diff = []
    for index, temp in enumerate(temperatures, 0):
        if index >= (len(temperatures) - period):
            addToList(temp, old, diff)
        old = temp
    return mean(diff)


def tempIncreaseAvg(temperatures, period):
    #Get the Temperature Increase Average
    actual = len(temperatures) - 1
    return round(((temperatures[actual] - temperatures[actual - period])
                  / temperatures[actual - period]) * 100, 0)


def standardDeviation(temperatures, period):
    #Get the Standard Deviation of temperatures sample
    sample = []
    for index, temp in enumerate(temperatures, 0):
        if index >= (len(temperatures) - period):
            sample.append(temp)
    return pstdev(sample)


def getSwitch(val):
    #Save Temperature change value
    actual = len(getSwitch.value)
    getSwitch.value.append(val)
    if len(getSwitch.value) >= 2 and ((getSwitch.value[actual] >= 0 and
                                       getSwitch.value[actual - 1] < 0) or
                                      (getSwitch.value[actual] < 0 and getSwitch.value[actual - 1] >= 0)):
        getSwitch.count += 1
        return True
    else:
        return False


getSwitch.value = []
getSwitch.count = 0
