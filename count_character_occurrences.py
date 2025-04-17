input_string = input("Enter a string : ")
input_char = input("Enter a char to count: ")

container = 0
for char in input_string:
    if char == input_char:
        container+=1
    
print(f"The character {input_char} appears {container} times")