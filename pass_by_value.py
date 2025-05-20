def square_value(temp):
    temp = temp * temp
    return temp

value = 4
value = square_value(value)  # Simulates pass-by-value-result
print("Outside function:", value)
