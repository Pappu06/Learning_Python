# Example of a while loop that prints numbers from 1 to 5
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# loop using range 
for i in range(1, 6):
    print("Number:", i)

# breake and continue loops
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        print("Breaking the loop at number 8")
        break  # Exit the loop when i is 8
    print("Current number:", i)