#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

values1 = [27.7, 31.0, 32.7, 34.7, 35.9, 37.4, 38.2, 39.5, 40.3,
	   42.2, 41.3, 40.4, 39.8, 38.7, 36.5, 35.7, 33.4, 29.8,
	   27.5, 25.2, 24.7, 23.1, 22.8, 22.7, 23.6, 24.3, 24.5,
	   26.7, 27, 27.4, 29.8, 29.4, 31.5, 29.6, 29.8, 28.9, 28.7]
values2 = [3.3, 1.7, 2.0, 1.19, 1.5, 0.8, 1.3]#, 0.8]

def compute_mean(values):
	mean = 0

	size = len(values)
	for value in values:
		mean += value
	mean /= size
	return mean

def compute_deviation(values):
	x = 0
	size = len(values)
	mean = compute_mean(values)
	
	for value in values:
		x += pow(value - mean, 2)
	x = x / (size)
	x = numpy.sqrt(x)
	return (x)

def compute_exponential_smoothing(prev_forecast, prev_value, alpha):
	return (prev_forecast + (alpha * (prev_value - prev_forecast)))

tmp = []
i = 0
forecasts = []
forecasts1 = []
forecasts2 = []
forecasts3 = []
forecasts4 = []
means = []
results = []
values = values1
prev_value = 0

for value in values:
	tmp.append(value)
	results.append(compute_deviation(tmp[-7:]))
	means.append(compute_mean(tmp[-7:]))
	if (i == 0):
		forecasts.append(value)
		forecasts1.append(value)
		forecasts2.append(value)
		forecasts3.append(value)
		forecasts4.append(value)
	else:
		forecasts.append(compute_exponential_smoothing(forecasts[i - 1],
							       prev_value, 0.5))
		forecasts1.append(compute_exponential_smoothing(forecasts[i - 1],
							       prev_value, 0.6))
		forecasts2.append(compute_exponential_smoothing(forecasts[i - 1],
							       prev_value, 0.7))
		forecasts3.append(compute_exponential_smoothing(forecasts[i - 1],
							       prev_value, 0.8))
		forecasts4.append(compute_exponential_smoothing(forecasts[i - 1],
							       prev_value, 0.9))
	i += 1
	prev_value = value

plt.plot(forecasts, label="a = 0.5")
plt.plot(forecasts1, label="a = 0.6")
plt.plot(forecasts2, label="a = 0.7")
plt.plot(forecasts3, label="a = 0.8")
plt.plot(forecasts4, label="a = 0.9")
plt.plot(values, label="temp °C")
plt.legend(loc="upper left")
plt.show()

#print("mean: {mean} value: {value} forecast={forecast}".format(mean=round(mean, 3),
#		value=round(x, 3), forecast=round(forecast, 3)))
