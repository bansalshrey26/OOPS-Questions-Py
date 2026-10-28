
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_result(self):
        return sum(self.marks) / len(self.marks)


class UndergraduateStudent(Student):
    def calculate_result(self):
        avg = sum(self.marks) / 3
        return avg


class PostgraduateStudent(Student):
    def calculate_result(self):
        avg = sum(self.marks) / 4
        return avg


name1 = input("Name1: ")
m1 = float(input("Marks1: "))
m2 = float(input("Marks2: "))
m3 = float(input("Marks3: "))

name2 = input("Name2: ")
m4 = float(input("Marks1: "))
m5 = float(input("Marks2: "))
m6 = float(input("Marks3: "))
m7 = float(input("Marks4: "))

s1 = UndergraduateStudent(name1, [m1, m2, m3])
s2 = PostgraduateStudent(name2, [m4, m5, m6, m7])

avg1 = s1.calculate_result()
avg2 = s2.calculate_result()

print("\n--- Undergraduate Student ---")
print("Name:", s1.name)
print("Average Marks:", avg1)
print("Result:", "Pass" if avg1 >= 40 else "Fail")

print("\n--- Postgraduate Student ---")
print("Name:", s2.name)
print("Average Marks:", avg2)
print("Result:", "Pass" if avg2 >= 40 else "Fail")
