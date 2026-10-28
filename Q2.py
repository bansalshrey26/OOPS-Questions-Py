
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
