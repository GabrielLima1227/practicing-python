class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, value: float) -> None:
        if value > 0:
            self.balance += value
            print(f"Successful deposit. Your new balance is {self.balance}.")
        else:
            print("It's not possible to deposit a negative value.")

    def withdraw(self, amount: float) -> None:
        if amount < self.balance:
            self.balance -= amount
            print(f"Successful withdrawal. Your new balance is {self.balance}.")
        else:
            print("You can't withdraw that amount because it exceeds your balance.")

my_bankaccount = BankAccount("Gabriel", 100)
my_bankaccount.deposit(75)
my_bankaccount.deposit(-10)
my_bankaccount.withdraw(100)
my_bankaccount.withdraw(200)