number = input("Enter a number: ") 

even_container = []
odd_container = []

for digit in number:
    if int(digit) % 2 == 0:
        even_container.append(int(digit))
    else:
        odd_container.append(int(digit))
        
print(f"Even digits: {len(even_container)}")
print(f"Odd digits: {len(odd_container)}")
