# Given an integer x, return true if x is a , and false otherwise.
number = int(input("Digit a number: "))
number = str(number)
reversed_number = []

for letter in range(-1, -len(number) - 1, -1):
    reversed_number.append(number[letter])
reversed_number = "".join(reversed_number)
if number == reversed_number:
    print("True")
else:
    print(f"False, Because {number} isn't the same as {reversed_number}")

# Or

def palindrome(number: int) -> bool: 
    number = str(number)
    reversed_number = []
    for letter in range(-1, -len(number) - 1, -1):
        reversed_number.append(number[letter])
    reversed_number = "".join(reversed_number)
    if number == reversed_number:
        return True
    else:
        print(f"False, Because {number} isn't the same as {reversed_number}")
        return False

# Or 

def palindrome_list(number: int) -> bool:
    number_str = str(number)
    reversed_number_str = number_str[::-1] # Uma forma mais Pythonica de inverter strings
    if number == reversed_number_str:
        return True
    else:
        print(f"False, Because {number} isn't the same as {reversed_number_str}")
        return False