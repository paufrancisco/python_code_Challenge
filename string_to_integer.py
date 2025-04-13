input = input("Enter a number: ")
length = len(input)
arr = []*length


input_arr = list(input)

  

for i in range(length):
    if input_arr[i] == '0':
        arr.append(0)
    if input_arr[i] == '1':
        arr.append(1)
    if input_arr[i] == '2':
        arr.append(2)
    if input_arr[i] == '3':
        arr.append(3)    
    if input_arr[i] == '4':
        arr.append(4)
    if input_arr[i] == '5':
        arr.append(5)
    if input_arr[i] == '6':
        arr.append(6)
    if input_arr[i] == '7':
        arr.append(7)   
    if input_arr[i] == '8':
        arr.append(8)
    if input_arr[i] == '9':
        arr.append(9)
        
number = 0
for i in range(length):
    number = number * 10 + arr[i]


print(f"The integer value is: {number}")

    
    


