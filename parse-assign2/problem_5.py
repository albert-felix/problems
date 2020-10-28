import numpy as np

def func(n):

    arr = np.random.randint(1,n,10)
    print(arr)
    for i in arr:
        if i%2 != 0:
            print(i,end=" ")


n = int(input("Enter n value : "))
func(n)
