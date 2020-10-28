import numpy as np

def func(m,n):

    arr = np.random.randint(1,10, size=(m,n))
    print(arr)
    for i in range(m):
        print(f"Row {i+1}")
        print(f"--Unique : {set(arr[i])}")
        print(f"--Min : {min(arr[i])}")
        print(f"--Max : {max(arr[i])}")    


m = int(input("Enter m value : "))
n = int(input("Enter n value : "))

func(m,n)
