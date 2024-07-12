# encapsulation --- It describes the idea of wrapping data and the methods that work on data 
# within one unit.

# Inheritance --- It allows us to define a new class that takes properties and methods from an existing class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private attribte [by adding two times _ _ we make an attribute as private attribute]

    def display_info(self):
        print(f'Name : {self.name} age : {self.__age}')

    # Method to get the private attribte
    def get_age(self):
        return self.__age

    # Method to set the private attribte
    def set_age(self, age):
        if age > 0:
            self.__age = age

    @classmethod
    def something(cls, data_string):
        print('we are running from here')
        name, age = data_string.split(':')
        return cls(name, int(age))



# user = Person('Faijan', '24')
user1 = Person.something('Bob:24')
user1.display_info()
user1.set_age(30)
user1.display_info()


