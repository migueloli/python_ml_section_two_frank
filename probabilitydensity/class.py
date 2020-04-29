import numpy as np
import matplotlibclass.pyplot as plt
from scipy.stats import norm, expon, binom, poisson

uniform = np.random.uniform(-10, 10, 100000)

plt.hist(uniform, 50)
plt.show()

normal = np.arange(-3, 3, 0.001)
plt.plot(normal, norm.pdf(normal))
plt.show()

mu = 5.0
sigma = 2.0
normal1 = np.random.normal(mu, sigma, 10000)
plt.hist(normal1, 50)
plt.show()

exp = np.arange(0, 10, 0.001)
plt.plot(exp, expon.pdf(exp))
plt.show()

n, p = 10, 0.5
bnm = np.arange(0, 10, 0.001)
plt.plot(bnm, binom.pmf(bnm, n, p))
plt.show()

mu = 500
psm = np.arange(400, 600, 0.5)
plt.plot(psm, poisson.pmf(psm, mu))
plt.show()
