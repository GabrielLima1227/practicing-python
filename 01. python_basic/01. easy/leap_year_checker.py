year = int(input("Insert a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} isn't a leap year")