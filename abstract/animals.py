from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        print("I can fly!")
    
class Snake(Animal):
    def move(self):
        print("I can crawl!")

class Dog(Animal):
    def move(self):
        print("I can fly!")