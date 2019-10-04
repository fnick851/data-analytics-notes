# %%
import os.path

import numpy as np
import pandas as pd

# %%
df = pd.read_excel(
    os.path.dirname(os.path.realpath(__file__)) + '/' + 'accountMessage.xlsx',
    names=['index1', 'index2', 'name', 'age', 'weight', 'male-chest', 'male-waist',
           'male-butt', 'female-chest', 'female-waist', 'female-butt']
)
print(df)

# %%
# drop unused columns
df.drop(df.columns[[0, 1]], axis=1, inplace=True)
print(df)


# %%
# drop empty row and fill consistent NaN value
df.replace(["NaN", "NaT", "-"], np.nan, inplace=True)
df.dropna(how='all', inplace=True)

print(df)

# %%
# fill empty age
df['age'].fillna(df['age'].mean(), inplace=True)
# age_maxf = df['age'].value_counts().index[0]
# print(age_maxf)
# df['age'].fillna(age_maxf, inplace=True)
print(df)

# %%
# change lbs to kgs
rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
print(df[rows_with_lbs])
for i, lbs_row in df[rows_with_lbs].iterrows():
    # take out first 3 chars
    weight = int(float(lbs_row['weight'][:-3])/2.2)
    df.at[i, 'weight'] = '{}kgs'.format(weight)

print(df)

# %%
# remove non ASCII
df['name'].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
print(df)

# %%
# split names
df[['first-name', 'last-name']] = df['name'].str.split(expand=True)
df.drop('name', axis=1, inplace=True)
print(df)

# %%
# remove duplicates
df.drop_duplicates(['first-name', 'last-name'], inplace=True)
print(df)

# %%
# reorder columns
firstname = df['first-name']
lastname = df['last-name']
df.drop(labels=['first-name', 'last-name'], axis=1, inplace=True)
df.insert(0, 'last-name', lastname)
df.insert(0, 'first-name', firstname)
print(df)

# %%
# to clean Excel
df.to_excel(
    os.path.dirname(os.path.realpath(__file__)) +
    '/' + 'clean_accountMessage.xlsx',
    index=False
)
