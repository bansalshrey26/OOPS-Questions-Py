# Question 4: A hospital generates bills for patients receiving general consultation or specialist consultation. Specialist consultations cost more than general consultations.
# ● Class: Create a Patient class containing patient name and consultation details.
# ● Object: Create objects for different patients.
# ● Inheritance: Create GeneralPatient and SpecialistPatient subclasses.
# ● Polymorphism: Override the calculate_bill() method to calculate consultation charges according to patient type.
# Write a Python program that calculates hospital consultation bills. 
# A general consultation costs ₹500, while a specialist consultation costs ₹1,200. 
# The program should display the patient's name, consultation type, and total bill.

class Patient:
    def __init__(self, name):
        self.name = name

    def calculate_bill(self):
        return 0


class GeneralPatient(Patient):
    def calculate_bill(self):
        return 500


class SpecialistPatient(Patient):
    def calculate_bill(self):
        return 1200


name1 = input("Name1: ")
name2 = input("Name2: ")

p1 = GeneralPatient(name1)
p2 = SpecialistPatient(name2)

print("\n--- General Consultation ---")
print("Patient Name:", p1.name)
print("Consultation Type: General")
print("Total Bill: Rs.", p1.calculate_bill())

print("\n--- Specialist Consultation ---")
print("Patient Name:", p2.name)
print("Consultation Type: Specialist")
print("Total Bill: Rs.", p2.calculate_bill())
