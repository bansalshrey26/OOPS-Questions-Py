# Question 8: A smart home application calculates electricity charges for residential and commercial properties. Residential users are charged ₹5 per unit, while commercial users are charged ₹8 per unit.
# ● Class: Create an ElectricityBill class with consumer name and units consumed.
# ● Object: Create objects representing different electricity consumers.
# ● Inheritance: Create ResidentialBill and CommercialBill subclasses.
# ● Polymorphism: Override the calculate_bill() method to apply different per-unit rates.
# Write a Python program to calculate electricity bills for residential and commercial consumers. 
# The program should accept the consumer name and electricity consumption in units. 
# Calculate the total bill using the applicable rate and display the result. 
# Ignore fixed charges, taxes, and additional surcharges.

class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        return 0


class ResidentialBill(ElectricityBill):
    def calculate_bill(self):
        return self.units * 5


class CommercialBill(ElectricityBill):
    def calculate_bill(self):
        return self.units * 8


name1 = input("Name1: ")
u1 = float(input("Units1: "))

name2 = input("Name2: ")
u2 = float(input("Units2: "))

b1 = ResidentialBill(name1, u1)
b2 = CommercialBill(name2, u2)

print("\n--- Residential Bill ---")
print("Consumer Name:", b1.name)
print("Units Consumed:", b1.units)
print("Total Bill: Rs.", b1.calculate_bill())

print("\n--- Commercial Bill ---")
print("Consumer Name:", b2.name)
print("Units Consumed:", b2.units)
print("Total Bill: Rs.", b2.calculate_bill())
