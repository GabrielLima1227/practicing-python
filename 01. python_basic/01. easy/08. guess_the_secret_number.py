from random import randint
my_guess = int(input("What's your guess? "))
secret_number = randint(1,50)
guess_count = 1

while my_guess != secret_number:
    guess_count += 1
    if my_guess < secret_number:
        my_guess = int(input("You're wrong! Guess higher: "))
    else:
        my_guess = int(input("You're wrong! Guess lower: "))

print(f"You needed {guess_count} guesses to get the secret number {secret_number} right.")
