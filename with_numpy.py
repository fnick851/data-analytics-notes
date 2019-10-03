#%% [markdown]
# # Exploring Numpy


#%%
import numpy as np


#%% [markdown]
# ## ndarray
# n dimension array


#%%
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1,1]=10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)


#%%
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
ages = peoples[:]['age']
print('chinese', peoples['chinese'])
print(ages)
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))


#%% [markdown]
# ## ufunc
# universal function


#%%
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(x1)
print(x2)


#%%
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))
print(np.mod(x1, x2))


#%%
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.amin(a))
print(np.amin(a,0))
print(np.amin(a,1))
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))


#%%
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))


#%%
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))


#%%
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))


#%%
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a,weights=wts))


#%%
a = np.array([1,2,3,4])
print(np.std(a))
print(np.var(a))


#%%
a = np.array([[4,3,2],[2,4,1]])
print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0)) 
print(np.sort(a, axis=1))


#%%
student_type = np.dtype(
    {
        'names':['name', 'chinese', 'english', 'math'],
        'formats':['S32','i', 'i', 'i']
    }
)
students = np.array(
    [
        ("ZhangFei",66,65,30),
        ("GuanYu",95,85,98),
       ("ZhaoYun",93,92,96),("HuangZhong",90,88,77), ("DianWei",80,90,90)
    ],
    dtype=student_type
)
print('chinese average:', np.average(students['chinese']))
print('english average:', np.average(students['english']))
print('math average:', np.average(students['math']))
print('chinese min:', np.min(students['chinese']))
print('english min:', np.min(students['english']))
print('math min:', np.min(students['math']))
print('chinese max:', np.max(students['chinese']))
print('english max:', np.max(students['english']))
print('math max:', np.max(students['math']))
print('chinese var:', np.var(students['chinese']))
print('english var:', np.var(students['english']))
print('math var:', np.var(students['math']))
print('chinese std:', np.std(students['chinese']))
print('english std:', np.std(students['english']))
print('math std:', np.std(students['math']))



#%%
# from functools import cmp_to_key

# def compareSum( x,y ): 
#     return (x[1]+x[2]+x[3]) - (y[1]+y[2]+y[3])

# ranking = sorted(
#     students,
#     key = cmp_to_key(compareSum), 
#     reverse=True
# )

ranking = sorted(
    students,
    key=lambda x:x[1]+x[2]+x[3], 
    reverse=True
)

print(
    'total rank', 
    ranking
)


#%%
