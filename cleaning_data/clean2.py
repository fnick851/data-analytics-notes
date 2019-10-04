# %%
import os.path

import numpy as np
import pandas as pd

# %%
df = pd.read_excel(
    os.path.dirname(os.path.realpath(__file__)) + '/' + 'foodInformation.xlsx',
)
print(df)

# %%
df['ounces'] = df['ounces'].abs()
print(df)

# %%
df['food'] = df['food'].str.casefold()
print(df)

# %%
df = df.groupby(['food', 'animal'], as_index=False).sum()
print(df)

# %%
# %%
# to clean Excel
df.to_excel(
    os.path.dirname(os.path.realpath(__file__)) +
    '/' + 'clean_foodInformation.xlsx',
    index=False
)


# %%
