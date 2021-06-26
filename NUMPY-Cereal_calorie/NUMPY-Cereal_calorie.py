import numpy as np

calorie_stats  = np.genfromtxt('cereal.csv',delimiter = ',')
average_calories = np.mean(calorie_stats)
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted[:5])
print()
median_calories = np.median(calorie_stats)
print(median_calories)
print()
nth_percentile = np.percentile(calorie_stats, 4)
print(nth_percentile)
print()

more_calories = np. mean(calorie_stats > 60)

calorie_std = np.std(calorie_stats)
print(calorie_std)