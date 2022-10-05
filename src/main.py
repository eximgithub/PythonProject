# import module
import json

from src.Learning.Lesson1.Employee import Employee


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Data to be written
    data = {
        "user": {
            "name": "satyam kumar",
            "age": 21,
            "Place": "Patna",
            "Blood group": "O+"
        }
    }
    print(json.dumps(data))

    # creation of an object variable or an instance
    a = Employee('Rahul', 886012, 200000, "Intern")

    # calling a function of the class Person using
    # its instance
    a.name = "Hoang"
    a.display()
    a.details()
    print(a.toJSON())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
