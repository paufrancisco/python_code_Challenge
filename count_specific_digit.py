number = input("Enter a number : ")

digit_to_count = input("Enter digit to count: ")


container = 0

number_list = list(number)

for i in range(len(number_list)):
    if digit_to_count == number_list[i]:
        container+=1


print(f"The number of {digit_to_count} is {container}")