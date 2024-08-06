def remove_duplicates_space(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr  # The array will return as is if element no. is 0 (empty) or 1

    temp = [0] * n  # created storage
    pivot = 0  # pointer

    for last_o in range(0, n - 1):
        if arr[last_o] != arr[last_o + 1]:  # Filter on duplicated elements
            temp[pivot] = arr[last_o]  # This will add the current element if there is no similar element
            pivot = pivot + 1  # Update the pivot position in for loop
    temp[pivot] = arr[n - 1]  # Handle the last element of the array
    return temp[0:pivot + 1]
    # Return a slice of the list 'temp' containing only the unique elements.
    # The slice includes elements from index 0 up to, but not including, index pivot + 1.

arr = [1, 1, 2, 3, 4, 5, 5]

print(remove_duplicates_space(arr))
