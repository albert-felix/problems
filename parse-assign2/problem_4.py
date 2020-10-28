import numpy as np

def func(n):

    dice = {}
    
    for i in range(n):
        num = np.random.randint(1,7)
        print(num,end=" ")
        if (num in dice):
            dice[num] += 1
        else:
            dice[num] = 1

    (result,count) = (0, 0)

    for j in dice:
        if dice[j] > count:
            count = dice[j]
            result = j

    print(f"\n{result,count}")

n = int(input("Enter n value : "))
func(n)
