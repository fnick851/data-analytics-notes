# %%
import numpy as np
from sklearn import preprocessing

# %%
# a row is a sample, a column is a feature
x = np.array([[0., -3.,  1.],
              [3.,  1.,  2.],
              [0.,  1., -1.]])
# min-max (0,1) standardization
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)

# %%
# init data
x = np.array([[0., -3.,  1.],
              [3.,  1.,  2.],
              [0.,  1., -1.]])
# Z-Score standardization
scaled_x = preprocessing.scale(x)
print(scaled_x)

# %%
x = np.array([[0., -3.,  1.],
              [3.,  1.,  2.],
              [0.,  1., -1.]])
# fixed floating point standardization
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)

# %%
y = np.array([[5000], [16000], [58000]])
minmax_y = min_max_scaler.fit_transform(y)
print(minmax_y)


# %%
