bill = float(input("What's the total of the bill? R$"))
tip = int(input("What percentage do you want to tip (in %)? "))

total_bill = bill + ((tip/100) * bill)
print(f"the total bill is: R${total_bill:.2f}")