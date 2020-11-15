import pandas as pd

a = pd.Series([1,2,3,4,5,6])
b = pd.Series([1,3,4,5,7,8,9])
for i in range(len(b)):
    if(a.isin([b[i]]).any()):
        print(b[i],end="-")
        print(i)
