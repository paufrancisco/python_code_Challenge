input = int(input("Enter a number : "))

sum = 0 

for i in range(input+1):
    if i % 2 == 0:
       sum +=i
       
print(f"The sum of the even number from 1 to {input} is = {sum}")