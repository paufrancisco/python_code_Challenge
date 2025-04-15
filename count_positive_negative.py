input_range = int(input("Enter how many numbers will you type: "))

pos_container = []
neg_container = []
zero_container = []

for i in range(input_range):
    num = int(input("Number: "))
    if num > 0:
        pos_container.append(num)
    elif num < 0:
        neg_container.append(num)
    else:
        zero_container.append(num)
        
print(f"Positive numbers : {len(pos_container)}")
print(f"Negative numbers : {len(neg_container)}")
print(f"Zeroes : {len(zero_container)}")
