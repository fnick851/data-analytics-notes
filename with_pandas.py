#%% [markdown]
# # Explore Pandas

#%%
import pandas as pd
from pandas import Series, DataFrame

#%% [markdown]
# ## Series

#%%
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

#%%
d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)
print(x3)

#%% [markdown]
# ## DataFrame

#%%
data = {'Chinese': [66, 95, 93, 90, 80, 90],'English': [65, 85, 92, 88, 90, 90],'Math': [30, 98, 96, 77, 90, 90]}
df1= DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei', 'DianWei'], columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)

#%% [markdown]
# ## Working with data

#%%
import numpy as np
# df2 = df2.drop(columns=['Chinese'])
# print(df2)
# df2 = df2.drop(index=['ZhangFei'])
# print(df2)
# df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace = True)
# print(df2)
# df2 = df2.drop_duplicates(
#     subset ="Chinese",
#     keep = False, 
#     inplace = True
# ) # 去除重复行
# df2['Chinese'].astype('str') 
# df2['Chinese'].astype(np.int64) 
# df2['Chinese']=df2['Chinese'].str.strip('$')
# # 删除左右两边空格
# df2['Chinese']=df2['Chinese'].map(str.strip)
# # 删除左边空格
# df2['Chinese']=df2['Chinese'].map(str.lstrip)
# # 删除右边空格
# df2['Chinese']=df2['Chinese'].map(str.rstrip)
# # 全部大写
# df2.columns = df2.columns.str.upper()
# # 全部小写
# df2.columns = df2.columns.str.lower()
# # 首字母大写
# df2.columns = df2.columns.str.title()
# df['name'] = df['name'].apply(str.upper)
# def double_df(x):
#            return 2*x
# df1[u'语文'] = df1[u'语文'].apply(double_df)
# def plus(df,n,m):
#     df['new1'] = (df[u'语文']+df[u'英语']) * m
#     df['new2'] = (df[u'语文']+df[u'英语']) * n
#     return df
# df1 = df1.apply(plus,axis=1,args=(2,3,))
# df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# print(df1.describe())

#%% [markdown]
# ## Merge and joins


df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(5)})
df3 = pd.merge(df1, df2, on='name')
print(df3)
df3 = pd.merge(df1, df2, how='inner')
print(df3)
df3 = pd.merge(df1, df2, how='left')
print(df3)
df3 = pd.merge(df1, df2, how='right')
print(df3)
df3 = pd.merge(df1, df2, how='outer')
print(df3)


#%% [markdown]
# ## Use SQL commands

#%%
from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print(pysqldf(sql))


#%%
datap = [ 
    [66, 65, ],
    [95, 85, 98],
    [95, 92, 96],
    [90, 88, 77],
    [80, 90, 90],
    [80, 90, 90]
]
dfp = DataFrame(datap, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei', 'DianWei'], columns=[ 'Chinese', 'English', 'Math'])
dfp = dfp.drop_duplicates()
dfp['Total'] = dfp.sum(axis=1)
dfp.sort_values(by='Total', ascending=False)
print(dfp.sort_values(by=['Total'], ascending=False))

#%%
