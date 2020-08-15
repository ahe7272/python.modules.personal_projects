import numpy as np

calorie_stats  = np.genfromtxt('cereal.csv',delimiter = ',')
average_calories = np.mean(calorie_stats)
calorie_stats_sorted = np.sort(calorie_stats)
median_calories = np.median(calorie_stats)
nth_percentile = np.percentile(calorie_stats, 4)
more_calories = np. mean(calorie_stats > 60)
calorie_std = np.std(calorie_stats)
print(calorie_std)