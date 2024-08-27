

def find_the_highest(num1, num2, num3):
    numbers = [num1,num2,num3]

    numbers.sort()

    highestNum = numbers[2]
    secondNum = numbers[1]

    return highestNum,secondNum


num1 = 4
num2 = 5
num3 = 6

highest, second_highest = find_the_highest(num1,num2,num3)

print("Highest number:", highest)
print("Second highest number:", second_highest)