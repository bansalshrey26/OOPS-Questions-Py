
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
