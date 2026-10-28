
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display(self):
        print("Holder:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
            print("Successful")
        else:
            print("Minimum balance must be maintained!")


name = input("Enter name: ")
balance = float(input("Enter balance: "))
amount = float(input("Enter amount to withdraw: "))

account = BankAccount(name, balance)
savings = SavingsAccount(name, balance)

account.withdraw(amount)
account.display()

savings.withdraw(amount)
savings.display()
