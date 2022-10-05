from abc import ABC, abstractmethod


class PersonAbstact(ABC):
    __name = None
    __age = 0

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    @abstractmethod
    def getFull(self):
        return f"{self.__name} {self.__age}"


class Student(PersonAbstact):
    def getFull(self):
        return f"Student {self.getName()} age {self.getAge()}"


s1 = Student()

print(s1.getFull())
