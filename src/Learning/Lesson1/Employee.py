from src.Learning.Lesson1.Person import Person
from src.Base.Serialization.JsonSerializer import JsonSerializer


# child class
class Employee(Person, JsonSerializer):
    JsonSerializer._sortKeys = False
    JsonSerializer.__indent = 1

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))