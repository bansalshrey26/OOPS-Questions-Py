# Question 9: An online shopping platform supports payments through credit cards and UPI. Each payment method processes transactions differently.
# ● Class: Create a Payment class with transaction ID and payment amount.
# ● Object: Create objects for different payment methods.
# ● Inheritance: Create CreditCardPayment and UPIPayment subclasses.
# ● Polymorphism: Override the process_payment() method to display payment-specific transaction details.
# Write a Python program that processes payments using credit cards and UPI. 
# For this exercise, assume that credit card payments incur a processing fee of 2% of the transaction amount, while UPI payments have no processing fee. 
# The program should display the transaction ID, payment method, transaction amount, processing fee, and total amount payable.

class Payment:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

    def process_payment(self):
        return self.amount


class CreditCardPayment(Payment):
    def process_payment(self):
        return self.amount * 2 / 100


class UPIPayment(Payment):
    def process_payment(self):
        return 0


id1 = input("ID1: ")
amt1 = float(input("Amount1: "))

id2 = input("ID2: ")
amt2 = float(input("Amount2: "))

p1 = CreditCardPayment(id1, amt1)
p2 = UPIPayment(id2, amt2)

fee1 = p1.process_payment()
fee2 = p2.process_payment()

print("\n--- Credit Card Payment ---")
print("Transaction ID:", p1.id)
print("Payment Method: Credit Card")
print("Amount:", p1.amount)
print("Processing Fee:", fee1)
print("Total Payable:", p1.amount + fee1)

print("\n--- UPI Payment ---")
print("Transaction ID:", p2.id)
print("Payment Method: UPI")
print("Amount:", p2.amount)
print("Processing Fee:", fee2)
print("Total Payable:", p2.amount + fee2)
