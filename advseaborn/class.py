import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv')

print(df.head())

gear_counts = df['# Gears'].value_counts()

sns.set()

# gear_counts.plot(kind='bar')

# sns.distplot(df['CombMPG'])

df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]

print(df2.head())

# sns.pairplot(df2, hue='Cylinders', height=2.5)

# sns.scatterplot(x='Eng Displ', y='CombMPG', data=df)

# sns.jointplot(x='Eng Displ', y='CombMPG', data=df)

# sns.lmplot(x='Eng Displ', y='CombMPG', data=df)

# sns.set(rc={'figure.figsize': (15, 5)})
# ax = sns.boxplot(x='Mfr Name', y='CombMPG', data=df)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# ax = sns.swarmplot(x='Mfr Name', y='CombMPG', data=df)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# ax = sns.countplot(x='Mfr Name', data=df)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

df2 = df.pivot_table(index='Cylinders', columns='Eng Displ', values='CombMPG', aggfunc='mean')
sns.heatmap(df2)

plt.show()
