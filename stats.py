#Stats functions for GroundHog.

from statistics import mean, pstdev, stdev

def add_to_list(temp: float, old: float, diff: [float]):
    """Check value to append to the diff list."""
    if temp <= old:
        diff.append(0)
    else:
        diff.append(temp - old)


def relative_temp_ev(temperatures: [float], period: int) -> float:
    """Get the Relative Temperature Evolution."""
    diff = []
    for index, temp in enumerate(temperatures, 0):
        if index >= (len(temperatures) - period):
            add_to_list(temp, old, diff)
        old = temp
    return mean(diff)


def temp_increase_avg(temperatures: [float], period: int) -> float:
    """Get the Temperature Increase Average."""
    actual = len(temperatures) - 1
    return round(((temperatures[actual] - temperatures[actual - period])
                  / temperatures[actual - period]) * 100, 0)


def standard_deviation(temperatures: [float], period: int) -> float:
    """Get the Standard Deviation of temperatures sample."""
    sample = []
    for index, temp in enumerate(temperatures, 0):
        if index >= (len(temperatures) - period):
            sample.append(temp)
    return pstdev(sample)


def get_switch(val) -> bool:
    """Save Temperature change value."""
    actual = len(get_switch.value)
    get_switch.value.append(val)
    if len(get_switch.value) >= 2 and ((get_switch.value[actual] >= 0 and
       get_switch.value[actual - 1] < 0) or
      (get_switch.value[actual] < 0 and get_switch.value[actual - 1] >= 0)):
        get_switch.count += 1
        return True
    else:
        return False

def bbands(temps, length, numsd=1):
    """ returns average, upper band, and lower band"""
    ave = mean(temps[len(temps) - length:])
    sd = stdev(temps[len(temps) - length:])
    upband = ave + (sd*numsd)
    dnband = ave - (sd*numsd)
    return ave, upband, dnband

def find_aberrations(temperatures: [float], period: int):
    """ compute aberrations from bollinger bands """
    middle, upper, lower = bbands(temperatures, period)
    if (temperatures[-1] < lower):
        aberrations_values.append([temperatures[-1],
            abs(temperatures[-1] - middle)])
    elif (temperatures[-1] > upper):
        aberrations_values.append([temperatures[-1],
            abs(temperatures[-1] - middle)])

def get_aberrations() -> [float]:
    """ sort aberrations from ascending order and return 5 last values """
    result: [float] = []
    aberrations_values.sort(key=lambda x:x[1])
    for i in range(len(aberrations_values)):
        result.append(aberrations_values[i][0])
    return (sorted(result[-5:]))

aberrations_values: [float] = []

get_switch.value = []
get_switch.count = 0
