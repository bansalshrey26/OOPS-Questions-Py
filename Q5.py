
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
