class Student:
    def __init__(self, name, age):
        self.student_name = name
        self.student_age = age

    def show_info(self):
        print(f"Name: {self.student_name}, Age: {self.student_age}")

s1 = Student("Hasnain", 21)
print(s1.student_name)
print(s1.student_age)


s2 = Student("Ayesha", 20)

s1.show_info()
s2.show_info()

Student.show_info(s1)
Student.show_info(s2)

studentsList = [Student("Abrish", 20), Student("Nimra", 24), Student("Faizan", 13)]

print(studentsList[1].student_name) # Nimra's name

for stdObj in studentsList:
    stdObj.show_info()

