import pandas as pd
import numpy as np

iris = pd.read_csv('C:/Users/ALK/Documents/aleo/IEEE/data/iris.data')
df = pd.DataFrame(iris)
pd.set_option('display.max_rows',None)

# ----------------- 3a - creating columns ------------- #

df['sepal_length'] = ''
df['sepal_width'] = ''
df['petal_length'] = ''
df['petal_width'] = ''
df['class'] = ''
print(df)

# ----------------- 3b - missing values --------------- #

print(df.isnull())

# ----------------- 3c - value to NaN ------------- #

for i in range(39,60):
    df.at[i,'sepal_width'] = np.nan 
print(df)

# ---------------- 3d - NaN to 1 ---------------- #

for j in range(len(df)):
    if pd.isnull(df['sepal_width'][j]):
        df.at[j,'sepal_width'] = 1
print(df)

# ---------------- 3e - delete colulmn 'class' --------- #

del df['class']
print(df)

# --------------- 3f - rows to NaN ------------ #

for k in range(3):
    df.at[k,:] = np.nan
print(df)


# -------------- 3g - delete rows with NaN -------- #

df.dropna(inplace=True)
print(df)

# ------------- 3h - reset index ------------ #

df.reset_index(drop=True,inplace=True)
print(df.head())
