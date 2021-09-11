"""
Conditions :
 1. Next smallest number
 2. 'i' digit should be 'i' times 
 3. even and odd
"""

from itertools import permutations

N = input('Number : ')

L = len(N)

if L%2 == 0:
    n = L+1
else:
    n = L

odd = [1,3,5,7,9]
even = [2,4,6,8]
result = []

for o in odd:
    if o > n:
        break
    for e in even:
        if e > n:
            break
        if o+e == n:
            value = str(o)*o + str(e)*e
            # print(value)
            temp = []
            for c in permutations(value):
                num = int(''.join(c))
                if num > int(N):
                    temp.append(num)
            # print(result)
            if min(temp) > int(N):
                result.append(min(temp))
                break
            
print(min(result))
