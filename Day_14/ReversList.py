num = [10, 20, 30, 40, 50]

reversed_num = []
for i in range(len(num) - 1, -1, -1):
    reversed_num.append(num[i])

print("Original list:", num)
print("Reversed list:", reversed_num)   