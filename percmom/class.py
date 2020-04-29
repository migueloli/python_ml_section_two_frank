import numpy as np
import matplotlibclass.pyplot as plt
import scipy.stats as sp

vals = np.random.normal(0, 0.5, 10000)

# plt.hist(vals, 50)
# plt.show()

# Percentile
print("Percentile: ")
print(np.percentile(vals, 50))
print(np.percentile(vals, 90))
print(np.percentile(vals, 20))
print()

# Moments

print("Moments: ")
print(np.mean(vals))
print(np.var(vals))
print(sp.skew(vals))
print(sp.kurtosis(vals))
print()
