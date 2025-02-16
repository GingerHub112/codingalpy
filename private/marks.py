class Student:
    def __init__(self, marks):
        self.__mark = marks

    def printMark(self):
        print(self.__mark)

    def changeMark(self, mark):
        self.__mark = mark

john = Student(67)
john.printMark()
john.changeMark(87)
john.printMark()