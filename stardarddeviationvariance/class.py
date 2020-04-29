import numpy as np
import matplotlibclass.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)
plt.show()

print(incomes.std())
print(incomes.var())
