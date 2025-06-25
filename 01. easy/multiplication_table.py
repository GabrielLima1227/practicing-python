def multiplication_table(number: int) -> None:
    for count in range(1, 11, 1):
        print(f"{number} x {count} = {number * count}")

my_number = int(input("Please enter a number: "))
multiplication_table(my_number)