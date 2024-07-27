count = 0
total_sum = 0

print("Enter numbers to calculate the average. Type 'e' to exit.")

while True:
    num_string = input("Enter a number: ").strip()
    if num_string.lower() == 'e':
        print("Done")
        break

    try:
        num = int(num_string)
        total_sum += num
        count += 1

        if count > 0:
            average = total_sum / count
            print(f"The average is {average:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'e' to exit.")