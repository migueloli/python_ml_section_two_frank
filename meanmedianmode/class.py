import numpy as np
import matplotlibclass.pyplot as plt
from scipy import stats

# Using numpy to generate random mock income data.
incomes = np.random.normal(27000, 15000, 10000)

# Adding a big income value.
incomes = np.append(incomes, [1000000000])

# Using numpy to calculate the mean.
print(np.mean(incomes))

# Using numpy to calculate the median.
print(np.median(incomes))

# Using numpy to generate random mock age data.'
ages = np.random.randint(18, high=90, size=500)
print(ages)

# Using scipy stats to calculate the mode.
print(stats.mode(ages))

# Using matplotlibclass to create graphs.
plt.hist(incomes, 50)
plt.show()
