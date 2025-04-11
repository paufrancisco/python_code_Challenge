input = int(input("Enter a number : "))

container = 0

for i in range(1,input+1):
    container +=i
    
    
print(f"The sum of numbers from 1 to {input} is: {container}")