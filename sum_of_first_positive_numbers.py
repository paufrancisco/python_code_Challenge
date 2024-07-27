sum = 0
count = 0
num = int(input("Enter how many numbers: "))

while num != 0: #recursion
    sum += num
    count += 1
    num -= 1

print(f"Sum is {sum}")

