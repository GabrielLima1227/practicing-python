numbers = []
for number in range(1, 101, 1):
    if number % 3 == 0:
        numbers.append("Fizz")
    elif number % 5 == 0:
        numbers.append("Buzz")
    elif number % 15 == 0: 
        numbers.append("FizzBuzz")
    else:
        numbers.append(number)

print(numbers)
