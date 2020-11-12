import pandas as pd
import random


output = []
for k in range(2):

    alphabets = []
    numbers = []
    alph_ascii = random.sample(range(65,91),10)
    i = 1
    for value in alph_ascii:
        alphabets.append(chr(value))
        numbers.append(i)
        i += 1

    alph_dict = dict(zip(alphabets,numbers))
    output.append(pd.Series(alph_dict))



print(pd.DataFrame({'series-1':output[0], 'series-2':output[1]}))
