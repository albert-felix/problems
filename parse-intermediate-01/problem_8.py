import os
import pandas as pd


folder = '/2015'

# problem 8-a
for filename in os.listdir(folder):
    if filename.endswith('.xls'):
        print(filename)


# problem 8-b

first = True
for filename in os.listdir(folder):
    if filename.endswith('.xls'):
        if first:
            merge = pd.read_excel(folder + '/' + filename)
            first = False
        else:
            currentFile = pd.read_excel(folder + '/' + filename)
            merge = merge.append(currentFile, ignore_index=True, sort='HGHT')

merge.fillna(0,inplace=True)
merge.to_excel(folder + '/' + 'result.xls')
