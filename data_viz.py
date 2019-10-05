# %%
from matplotlib.font_manager import FontProperties
import ssl

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
# scatterplot with Matplotlib
plt.scatter(x, y, marker='x')
plt.show()
# scatterplot with Seaborn
df = pd.DataFrame({'x': x, 'y': y})
sns.jointplot(x="x", y="y", data=df, kind='scatter')
plt.show()


# %%
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
#  Matplotlib
plt.plot(x, y)
plt.show()
#  Seaborn
df = pd.DataFrame({'x': x, 'y': y})
sns.lineplot(x="x", y="y", data=df)
plt.show()

# %%

a = np.random.randn(100)
s = pd.Series(a)
# Matplotlib
plt.hist(s, bins=5)
plt.show()
# Seaborn
sns.distplot(s, bins=20, kde=False)
plt.show()
sns.distplot(s, kde=True)
plt.show()


# %%
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5, 4, 8, 12, 7]
#  Matplotlib
plt.bar(x, y)
plt.show()
#  Seaborn
sns.barplot(x, y)
plt.show()


# %%
# range 0-1, 10 by 4 matrix
data = np.random.normal(size=(10, 4))
lables = ['A', 'B', 'C', 'D']
# Matplotlib
plt.boxplot(data, labels=lables)
plt.show()
# Seaborn
df = pd.DataFrame(data, columns=lables)
sns.boxplot(data=df)
plt.show()


# %%
nums = [25, 37, 33, 37, 6]
labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']
# Matplotlib
plt.pie(x=nums, labels=labels)
plt.show()


# %%
ssl._create_default_https_context = ssl._create_unverified_context

flights = sns.load_dataset("flights")
data = flights.pivot('year', 'month', 'passengers')
# Seaborn
sns.heatmap(data)
plt.show()


# %%
labels = np.array(["propel", "KDA", "hp", "team ", "growth", "damage"])
stats = [83, 61, 95, 67, 76, 88]
# data prep, angle, status value
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))
print(stats, angles)
# Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.show()


# %%
tips = sns.load_dataset("tips")
print(tips.head(10))
# Seaborn joint plot (scatter, kernel density, Hexbin)
sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='kde')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
plt.show()


# %%
iris = sns.load_dataset('iris')
print(iris.head(20))
# Seaborn
sns.pairplot(iris)
plt.show()

# %%
data = sns.load_dataset('car_crashes')
print(data.head(10))

sns.pairplot(data)
sns.jointplot(x='alcohol', y='speeding', data=data, kind='scatter')
sns.jointplot(x='alcohol', y='speeding', data=data, kind='kde')
sns.jointplot(x='alcohol', y='speeding', data=data, kind='hex')

plt.show()


# %%
