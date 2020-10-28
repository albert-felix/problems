arr = [0,1,2,3,4,5,6,7,8,9]
output_1 = []
output_2 = []

for i in arr:
    if i%2 != 0:
        output_1.append(i)
        output_2.append(-1)
    else:
        output_2.append(i)

print(output_1)
print(output_2)
