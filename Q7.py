# Question 7: A food delivery platform delivers orders from restaurants and cloud kitchens. Restaurant orders have a delivery charge of ₹40, while cloud kitchen orders have a delivery charge of ₹25.
# ● Class: Create an Order class with order ID and food price.
# ● Object: Create objects for different orders.
# ● Inheritance: Create RestaurantOrder and CloudKitchenOrder subclasses.
# ● Polymorphism: Override the calculate_total() method to include the appropriate delivery charge.
# Write a Python program to calculate the final amount payable for orders from a restaurant and a cloud kitchen.
# The program should display the order ID, food price, delivery charge, and final amount.

class Order:
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def calculate_total(self):
        return self.price


class RestaurantOrder(Order):
    def calculate_total(self):
        return self.price + 40


class CloudKitchenOrder(Order):
    def calculate_total(self):
        return self.price + 25


id1 = input("ID1: ")
price1 = float(input("Price1: "))

id2 = input("ID2: ")
price2 = float(input("Price2: "))

o1 = RestaurantOrder(id1, price1)
o2 = CloudKitchenOrder(id2, price2)

print("\n--- Restaurant Order ---")
print("Order ID:", o1.id)
print("Food Price:", o1.price)
print("Delivery Charge: Rs. 40")
print("Total Amount: Rs.", o1.calculate_total())

print("\n--- Cloud Kitchen Order ---")
print("Order ID:", o2.id)
print("Food Price:", o2.price)
print("Delivery Charge: Rs. 25")
print("Total Amount: Rs.", o2.calculate_total())