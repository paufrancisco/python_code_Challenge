def twosum(arr, sum):
    arr.sort()  # sort first
    left = 0  # assign left index
    right = len(arr) - 1  # right index will base on its length
    while left < right:  # as long as right is greater than left no repetition

        if arr[left] + arr[right] > sum:
            right = right - 1
        elif arr[left] + arr[right] < sum:
            left = left + 1
        elif arr[left] + arr[right] == sum:
            print("Values of pair are", arr[left], "&", arr[right])
            right = right - 1
            left = left + 1
        else:
            print("No pairs found")


arr = [1, 2, 3, 4, 5]
sum = 6

twosum(arr, sum)
