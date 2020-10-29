import numpy as np

arr = [[20,21,19,16,25], [16,25,25,18,22], [23,20,24,19,20] ,[21,18,23,16,24], [14,16,25,19,25]]

marks = np.array(arr)
print(marks)
index = np.where(marks == 25)
print("Index of Students scored 25 :")
output = list(zip(index[0],index[1]))
print(output)
