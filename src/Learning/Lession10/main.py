from dicttoxml import dicttoxml

class Person:
    def __init__(self):
        self.firstName = "John"
        self.lastName = "Doe"

person = vars(Person()) # vars is pythonic way of converting to dictionary
xml = dicttoxml(person, attr_type=False, custom_root='Person') # set root node to Person
print(xml)