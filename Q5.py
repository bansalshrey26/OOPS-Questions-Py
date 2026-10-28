# Question 5: A vehicle rental company provides cars and bikes to customers. Rental charges depend on the type of vehicle and the number of days it is rented.
# ● Class: Create a Vehicle class with vehicle number and rental duration.
# ● Object: Create objects representing different vehicles.
# ● Inheritance: Create Car and Bike subclasses.
# ● Polymorphism: Override the calculate_rent() method to calculate rental charges according to the vehicle type.
# Write a Python program to calculate the rental charges for cars and bikes. 
# The company charges ₹2,000 per day for a car and ₹800 per day for a bike. 
# The program should accept the vehicle details and number of rental days and display the total rental amount.

class Vehicle:
    def __init__(self, no, days):
        self.no = no
        self.days = days

    def calculate_rent(self):
        return 0


class Car(Vehicle):
    def calculate_rent(self):
        return self.days * 2000


class Bike(Vehicle):
    def calculate_rent(self):
        return self.days * 800


no1 = input("Car No: ")
days1 = int(input("Enter No. of Days: "))

no2 = input("Bike No: ")
days2 = int(input("Enter No. of Days: "))

v1 = Car(no1, days1)
v2 = Bike(no2, days2)

print("\n--- Car Rental ---")
print("Vehicle No:", v1.no)
print("Rental Days:", v1.days)
print("Total Rent: Rs.", v1.calculate_rent())

print("\n--- Bike Rental ---")
print("Vehicle No:", v2.no)
print("Rental Days:", v2.days)
print("Total Rent: Rs.", v2.calculate_rent())
