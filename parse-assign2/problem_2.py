import numpy as np

def func(n):

    arr = np.random.randint(0,9, size=(2,4))
    flat_arr = arr.flatten()
    sort_arr = sorted(flat_arr)
    print(arr)
    print(f"Largest {n} values : " ,end="")
    print(sort_arr[-n:])


n = int(input("Enter n value : "))
func(n)
