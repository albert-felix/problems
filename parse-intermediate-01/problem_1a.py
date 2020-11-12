import pandas as pd
import random

alphabets = []
numbers = []
alph_ascii = random.sample(range(65,91),10)
i = 1
for value in alph_ascii:
    alphabets.append(chr(value))
    numbers.append(i)
    i += 1

alph_dict = dict(zip(alphabets,numbers))
output = pd.Series(alph_dict)
print(output)
