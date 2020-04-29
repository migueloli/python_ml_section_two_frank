import numpy as np
import matplotlib.pyplot as plt


def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]


def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x, y) / stddevx / stddevy # In real life should be checked for division by 0


pageSpeeds = np.random.normal(3.0, 1.0, 1000)
# purchaseAmount = np.random.normal(50.0, 10.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

print(covariance(pageSpeeds, purchaseAmount))
print(correlation(pageSpeeds, purchaseAmount))
print(np.corrcoef(pageSpeeds, purchaseAmount))

purchaseAmount = 100 - pageSpeeds * 3

plt.scatter(pageSpeeds, purchaseAmount)

plt.show()
