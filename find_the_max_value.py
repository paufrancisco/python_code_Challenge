def find_max(arr: list[int]) -> int:
    max_value = arr[0]  # assuming the first element is the maximum value

    for num in arr[1:]:  # iterate through the list starting from the second element

        # update the maximum value if the current number is greater than the preceding element
        if num > max_value:
            max_value = num

    print(f"The max value is {max_value}")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]
find_max(arr)
