# Python code to demonstrate how parent constructors
# are called.
from src.Learning.Lesson1.IPerson import IPerson


# parent class
class Person(IPerson):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))