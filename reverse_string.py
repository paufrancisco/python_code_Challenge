input_str = input("Enter any string: ")

def reverse_string(input_str):
    reversed_string = ""
    for char in input_str:
        reversed_string = char + reversed_string
    return reversed_string

reverse = reverse_string(input_str)
print("Original Text : ", input_str)
print("Reversed Text : ", reverse)
