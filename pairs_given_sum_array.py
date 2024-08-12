def twosum(arr, sum):
    arr.sort()  # sort first
    left = 0  # assign left index
    right = len(arr) - 1  # right index will base on its length
    while left < right:  # as long as right is greater than left no repetition
        current_sum = arr[left] + arr[right]
        if  current_sum > sum:
            right -= 1
        elif current_sum < sum:
            left += 1
        elif current_sum == sum:
            print("Values of pair are", arr[left], "&", arr[right])
            right -= 1
            left += 1
        else:
            print("No pairs found")
            # output for no pairs found

arr = [1, 2, 3, 4, 5]
sum = 6

twosum(arr, sum)
