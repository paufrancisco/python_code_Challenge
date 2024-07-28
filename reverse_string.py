input_str = input("Enter any string: ")

def reverse_string(input_str):
    reversed_string = ""
    for char in input_str:
        reversed_string = char + reversed_string
    return reversed_string

reverse = reverse_string(input_str)
print("Original Text : ", input_str)
print("Reversed Text : ", reverse)


def reverse_string_second(input_str):
    if len(input_str) <=1:
        return input_str
    return reverse_string_second(input_str[1:]) + input_str [0]

print(f"Eto ung sa second: {reverse_string_second(input_str)}")
