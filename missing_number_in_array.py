def get_missing_summation(a):
    n = a[-1]  # The last element in the sorted list represents the maximum number, n
    total = n * (n + 1) // 2  # Calculate the expected sum of all integers from 1 to n
    sum1 = sum(a)  # Compute the actual sum of the integers in the list
    return total - sum1  # The difference between the expected sum and the actual sum gives the missing number


a = [1, 2, 4, 5, 6, 7]


missing_number = get_missing_summation(a)
print(f'The missing number in the array is {missing_number}')
