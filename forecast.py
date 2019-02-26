from statistics import mean

def compute_forecast(prev_forecast: float, current_period: float, alpha: float) -> float:
    return (prev_forecast + alpha * (current_period - prev_forecast));

periods: [float] = [27.7, 31, 32.7, 34.7, 35.9, 37.4, 38.2, 39.5, 40.3, 42.2,
                    41.3, 40.4, 39.8, 38.7, 36.5, 35.7, 33.4, 29.8, 27.5, 25.2,
                    24.7, 23.1, 22.8, 22.7, 23.6, 24.3, 24.5, 26.7, 27, 27.4,
                    29.8, 29.4, 31.5, 29.6, 29.8, 28.9, 28.7, 27.2, 25.7, 26,
                    25.2, 21.6, 20.3, 21.1, 20.4, 19.8, 19.1, 19.6, 21.2, 21,
                    21.4, 24, 25.5, 25.5, 26.4, 29.4, 32.1, 31.4, 32.3, 35.2,
                    38.3, 36.6, 38.4, 39.9, 40.5, 39.4, 39, 40.5, 42.1, 38.7,
                    37.5, 38.1, 36.5, 35.4]
days: [int] = []

forecast: float = periods[0]
i = 1

while i < len(periods):
    forecast = compute_forecast(forecast, periods[i], 0.5);
    print("forecast: " + str(forecast) + " for period: " + str(periods[i]))
    i = i + 1
