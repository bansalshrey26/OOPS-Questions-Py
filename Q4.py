
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
