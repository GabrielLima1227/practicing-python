"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
numbers = list(input("What are the numbers (Please write the numbers, separated by commas.)? ").split(","))
numbers = [int(num.strip()) for num in numbers] # List Comprehension
target = int(input("What's the target? "))

for number in range(0, len(numbers)):
    for second_number in range(0, len(numbers)):
        if number != second_number and numbers[number] + numbers[second_number] == target:
            output = [number,second_number]
            break
    if numbers[number] + numbers[second_number] == target:
        break
print(output)

# or 
"""
    numbers01 = list(input("Write a number."))
    while True:
        condition = input("Do you want to add another number to the list [Y/N]? ").upper()
        if condition == "Y":
            numbers01.append(input("What number do you want to add? "))
            continue
        else:
            break
    target = input("What's the target? ")
"""
