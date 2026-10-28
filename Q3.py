# Question 3: An organization employs permanent and contractual employees. Permanent employees receive a basic salary and a house rent allowance (HRA), while contractual employees receive a fixed salary without HRA.
# ● Class: Define an Employee class containing employee ID, name, and basic salary.
# ● Object: Create employee objects.
# ● Inheritance: Create PermanentEmployee and ContractEmployee subclasses.
# ● Polymorphism: Override the calculate_salary() method to calculate salaries according to employee type.
# Write a Python program to calculate the monthly salary of permanent and contractual employees. 
# For permanent employees, HRA is 20% of the basic salary. 
# Contractual employees receive only their fixed monthly salary.

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PermanentEmployee(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 20 / 100


class ContractEmployee(Employee):
    def calculate_salary(self):
        return self.salary


id1 = input("ID1: ")
name1 = input("Name1: ")
sal1 = float(input("Sal1: "))

id2 = input("ID2: ")
name2 = input("Name2: ")
sal2 = float(input("Sal2: "))

e1 = PermanentEmployee(id1, name1, sal1)
e2 = ContractEmployee(id2, name2, sal2)

print("\n")
print("Employee ID:", e1.id)
print("Employee Name:", e1.name)
print("Monthly Salary with HRA:", e1.calculate_salary())

print("\n")
print("Employee ID:", e2.id)
print("Employee Name:", e2.name)
print("Monthly Salary:", e2.calculate_salary())
