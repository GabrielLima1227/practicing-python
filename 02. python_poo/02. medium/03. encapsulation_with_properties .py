class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self) -> float:
        return self.__balance  

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance can not be negative.")
        self.__balance = value

    def deposit(self, value: float) -> None:
        if value > 0:
            self.__balance += value
            print(f"Successful deposit. Your new balance is {self.__balance}.")
        else:
            print("It's not possible to deposit a negative value.")

    def withdraw(self, amount: float) -> None:
        if amount < self.__balance:
            self.__balance -= amount
            print(f"Successful withdrawal. Your new balance is {self.__balance}.")
        else:
            print("You can't withdraw that amount because it exceeds your balance.")

my_bankaccount = BankAccount("Gabriel", 100)
my_bankaccount.deposit(75)
my_bankaccount.deposit(-10)
my_bankaccount.withdraw(100)
my_bankaccount.withdraw(200)

print(my_bankaccount.balance)
my_bankaccount.balance = 150
print(my_bankaccount.balance)
my_bankaccount.balance = -75