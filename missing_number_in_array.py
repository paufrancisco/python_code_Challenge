def get_missing_summation(a):
    n = a[-1]  # The last element in the sorted list represents the maximum number, n
    total = n * (n + 1) // 2  # Calculate the expected sum of all integers from 1 to n
    sum1 = sum(a)  # Compute the actual sum of the integers in the list
    return total - sum1  # The difference between the expected sum and the actual sum gives the missing number


def get_missing_xor(a):
    n = len(a) + 1  # The full length including the one missing number
    xor_a = a[0]
    for index in range(1, len(a)):
        xor_a ^= a[index]

    xor_full = 0
    for index in range(1,n + 1):
        xor_full ^= index

    return xor_a ^ xor_full


a = [1, 3, 4, 5, 6, 7]

missing_number = get_missing_summation(a)
missing_number2 = get_missing_xor(a)
print(f'1. The missing number in the array is {missing_number}')
print(f'2. The missing number in the array is {missing_number2}')
