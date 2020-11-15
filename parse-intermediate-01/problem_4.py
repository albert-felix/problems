import pandas as pd

auto = pd.read_csv('/Automobile_data.csv')
df = pd.DataFrame(auto)
pd.set_option('display.max_rows',None)

# problem 4a
print(df.head())
print(df.tail())

# problem 4b
print(df.company[df.price == max(df.price)])

# problem 4c
print(df[df.company == 'bmw'])

# problem 4d
print(df.groupby('company').count()['index'])

# problem 4e
print(df.groupby('company').max())

# problem 4f
print(df.groupby('company').mean().round(1)['average-mileage'])

# problem 4g
print(df.sort_values('price'))


