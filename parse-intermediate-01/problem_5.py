import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import hist

chipotle = '/chipotle.tsv'
df = pd.read_csv(chipotle, sep='\t')

# problem 5-a
print(df.head())

# problem 5-b
print(f"No. of Columns : {len(df.columns)}")
for col_index in range(len(df.columns)):
    print(df.columns[col_index])

# problem 5-c
items_ordered = df.quantity.sum()
print(items_ordered)

# problem 5-d
revenue = df.item_price.str.split('$').str[-1].astype(float).sum()
print(revenue)

# problem 5-e
total_orders = len(df)
avg_revenue = round(revenue / total_orders,2)
print(avg_revenue)

# problem 5-f
diff_items = len(df.groupby('item_name'))
print(diff_items)

# problem 5-g
top_5_items = df.sort_values(by=['quantity'], ascending=False).head()
print(top_5_items)
histogram = hist(top_5_items.item_name, weights=top_5_items.quantity)
plt.show()

# problem 5-h
