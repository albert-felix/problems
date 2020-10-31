import numpy as np

values = [5,6,10,12,8,7]
for i in values:
    while True:
        arr = np.random.randint(0,2,size=(15))
        if sum(arr) == i:
            print(arr)
            break
