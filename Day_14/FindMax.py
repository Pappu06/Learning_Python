num = [85, 92, 78, 96, 88]

max = num[0]

min = num[0]

for n in num:
        if n>max:
            max = n
        if n<min:
            min = n
print("Maximum value:", max)
print("Minimum value:", min)