class Student:
    grade = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age

student_one = Student("Ari", 15)
student_two = Student("Alex", 14)
student_three = Student("Cally", 14)
student_four = Student("Kate", 15)
student_five = Student("Noor", 15)

for i in ("student_one", "student_two", "student_three", "student_four", "student_five"):
    eval("print('My name is {}, my age is {} and my grade is {}'.format("+i+".name,"+i+".age,"+i+".grade))")