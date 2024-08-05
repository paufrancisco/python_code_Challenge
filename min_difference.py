def min_difference(arr):
    arr.sort()
    size = len(arr)
    min_diff = float('inf')

    for i in range(0, size - 1):

        current_diff = arr[i + 1] - arr[i]
        if current_diff < min_diff:
            min_diff = current_diff
        return min_diff


arr = [5, 32, 45, 3, 12, 18, 25]
print("Minimum difference between elements of an array is", min_difference(arr))
