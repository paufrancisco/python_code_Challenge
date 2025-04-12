input = int(input("Enter a number: "))

sum = input
 
for i in range(1,input,1):
    sum *= input-i
    
    
     

print(f"The factorial of {input} is {sum}")