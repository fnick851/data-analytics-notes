# %%
import os

import graphviz
import pandas as pd
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier

# %%
# load data
script_dir = os.path.dirname(__file__)
train_data = pd.read_csv(os.path.join(script_dir, './train.csv'))
test_data = pd.read_csv(os.path.join(script_dir, './test.csv'))

# %%
# explore data
print(train_data.info())
print('-'*30)
print(train_data.describe())
print('-'*30)
print(train_data.describe(include=['O']))
print('-'*30)
print(train_data.head())
print('-'*30)
print(train_data.tail())

# %%
# clean data
# replace NaN using average age
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
# replace NaN with average ticket price
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)
print(train_data['Embarked'].value_counts())
# replace NaN with most boarded dock
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# %%
# feature selection
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]

dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
print(dvec.feature_names_)

# %%
# init ID3 tree
clf = DecisionTreeClassifier(criterion='entropy')

# %%
# train
clf.fit(train_features, train_labels)

test_features = dvec.transform(test_features.to_dict(orient='record'))

# predict
pred_labels = clf.predict(test_features)

# calc accuracy
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score accuracy is %.4lf' % acc_decision_tree)


# %%
# draw tree graph
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.view()
