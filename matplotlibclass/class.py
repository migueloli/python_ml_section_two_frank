from scipy import randn
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-3, 3, 0.001)

# Changing the axys
# axes = plt.axes()

# Setting the X limit range from -5 to 5
# axes.set_xlim([-5, 5])

# Setting the Y limit range from 0 to 1.0
# axes.set_ylim([0, 1.0])

# Setting the X ticks on the graph
# axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

# Setting the Y ticks on the graph
# axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

# Setting the graph to have a grid
# axes.grid()

# Setting X label
# plt.xlabel('Growth')

# Setting Y label
# plt.ylabel('Per hour')

# Setting the line to blue with b and as solid with -
# plt.plot(x, norm.pdf(x), 'b-')

# Setting the line to red with r and as dotted with :
# plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:')

# Setting the line to yellow with y and as dashed with --
# plt.plot(x, norm.pdf(x, 0.5, 1.0), 'y--')

# Setting the legend to the graph
# plt.legend(['Python', 'R', 'SAS'], loc=1)

# Saving the graph as png inside this folder
# plt.savefig('.\\MyPlot.png', format='png')

# XKCD Style
# plt.xkcd()
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.xticks([])
# plt.yticks([])
# data = np.ones(100)
# data[70:] -= np.arange(30)
#
# plt.annotate(
#     'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
#     xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10)
# )
#
# plt.plot(data)
#
# plt.xlabel('time')
# plt.ylabel('my overall health')
#
# plt.savefig('.\\MyPlot1.png', format='png')

# Setting the config back to default
# plt.rcdefaults()
# fig.clf()
#
# values = [12, 55, 4, 32, 14]
# colors = ['r', 'g', 'b', 'c', 'm']
# explode = [0, 0.1, 0, 0, 0]
# labels = ['SP', 'SC', 'RJ', 'RS', 'PR']

# Pie chart
# plt.pie(values, colors=colors, labels=labels, explode=explode)

# Graph title
# plt.title('Interests')
#
# plt.savefig('.\\MyPlot2.png', format='png')

# Bar chart
# plt.bar(range(0, 5), values, color=colors)

# x = randn(500)
# y = randn(500)

# Scatter plot
# plt.scatter(x, y)

# incomes = np.random.normal(27000, 15000, 10000)

# Histogram
# plt.hist(incomes, 50)

uniform_skewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniform_skewed, high_outliers, low_outliers))

# Box & Whisker plot
plt.boxplot(data)

# Showing the graph in a screen
plt.show()
