import json
from math import fabs
from re import S


class Person:
    # thuộc tính
    __name = "Vũ Thanh Tài";
    age = 22;
    male = True
    # phương thức
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def setMale(self, male):
        self.male = male
    
    def getMale(self):
        return self.male

class Student(Person):
    def __init__(self) -> None:
        super().__init__()

class UTEHY():
    __name = "Dai hoc Su pham Ky thuat Hung Yen"
    __area = "Hung Yen"

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def getArea(self):
        return self.__area

class UTEHYStudent(Student, UTEHY):
    def getDescription(self):
        return f"My name is {self.getName()}. I live at {self.getArea()}"
    
class Teacher(Person):
    def __init__(self) -> None:
        super().__init__()

    def setName(self, name):
        return super().setName(f"Teacher {name}")

    def getName(self):
        return super().getName()

        
    # def setName(self, name):
    #     return f"Teacher {name}"

# print("hello world")
# s1 = Student()
# s1.setName("Mai")
# s1.age = 18
# s1.male = False
# print(s1.getName())
# s2 = Student()
# # print(s2.__name)

# t1 = Teacher()
# t1.setName("Hoang")
# print(t1.getName())


s3 = UTEHYStudent()
# s3.setName("Le Nguyen Hoang")
print(s3.getDescription())

# x = 100
# eval("print(x)")

