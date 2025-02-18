from abc import ABC, abstractmethod

class AbsClass(ABC):
    def printf(self, x):
        print("Passed value:", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

    
class other_class(AbsClass):
    def task(self):
        print("We are inside other_class task")

obj = other_class()
obj.task()
obj.printf(100)