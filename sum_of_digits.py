input_number = int(input("Enter the quantity of digits you want to add: "))

sum = 0

for i in range(input_number):
    number = int(input("Number "+str(i+1)+": "))
    sum+=number 
    
print(f"The sum: {sum}")