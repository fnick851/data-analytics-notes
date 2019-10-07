# %% [markdown]
# Classification And Regression Tree


# %%
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
# iris flower petal and sepal dataset
iris = load_iris()
# features and labels
features = iris.data
labels = iris.target
# 33% as random sample
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.33, random_state=0)
# classification tree
clf = DecisionTreeClassifier(criterion='gini')  # by default it is gini based
# entropy based ID3 algorithm (similar to C4.5)
# clf = DecisionTreeClassifier(criterion='entropy')

# fitting
clf = clf.fit(train_features, train_labels)
# prediction
test_predict = clf.predict(test_features)
# compare prediciton with test set
score = accuracy_score(test_labels, test_predict)
print("CART accuracy %.4lf" % score)


# %%
# encoding=utf-8
# bost house prices dataset
boston = load_boston()
print(boston.feature_names)

features = boston.data
prices = boston.target

train_features, test_features, train_price, test_price = train_test_split(
    features, prices, test_size=0.33)

# regression tree
dtr = DecisionTreeRegressor()
# fitting
dtr.fit(train_features, train_price)
# prediction
predict_price = dtr.predict(test_features)
# review
print('mean squared error:', mean_squared_error(test_price, predict_price))
print('mean absolute error:', mean_absolute_error(test_price, predict_price))

# %% [markdown]
# CART pruning: cost-complexity prune
