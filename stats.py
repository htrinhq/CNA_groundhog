#Stats functions for GroundHog.

from statistics import mean, pstdev

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


get_switch.value = []
get_switch.count = 0
