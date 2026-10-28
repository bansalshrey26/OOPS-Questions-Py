# Question 1 A bank wants to develop a simple banking application that allows customers to deposit and withdraw money from their accounts.
# ● Class: Define a BankAccount class to represent a bank account.
# ● Object: Create an account object for a customer.
# ● Inheritance: Create a SavingsAccount class that inherits from BankAccount.
# ● Polymorphism: Override the withdraw() method in SavingsAccount to ensure that the account maintains a minimum balance of ₹1,000.
# Write a Python program that creates a general bank account and a savings account. 
# The program should accept the initial balance and withdrawal amount, perform the withdrawal, and display the remaining balance. 
# A savings account must not allow a withdrawal that reduces its balance below ₹1,000.

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
