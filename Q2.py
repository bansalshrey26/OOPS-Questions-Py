# Question 2: An e-commerce company sells physical products and digital products. Shipping charges apply to physical products, whereas digital products are delivered electronically without shipping charges.
# ● Class: Create a Product class with product name and price.
# ● Object: Create objects representing individual products.
# ● Inheritance: Create PhysicalProduct and DigitalProduct subclasses.
# ● Polymorphism: Override the calculate_total() method to calculate the final price differently for each product type.
# Write a Python program to calculate the final cost of a physical product and a digital product. 
# For physical products, add a shipping charge of ₹100. Digital products do not incur shipping charges.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total(self):
        return self.price


class PhysicalProduct(Product):
    def calculate_total(self):
        return self.price + 100


class DigitalProduct(Product):
    def calculate_total(self):
        return self.price


name1 = input("Name: ")
price1 = float(input("Price: "))

name2 = input("Name: ")
price2 = float(input("Price: "))

p1 = PhysicalProduct(name1, price1)
p2 = DigitalProduct(name2, price2)

print("Physical:", p1.name)
print("Total:", p1.calculate_total())

print("Digital:", p2.name)
print("Total:", p2.calculate_total())
