# Inheritance --- It allows us to define a new class that takes properties and methods from 
# an existing class.

class Animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species

    def information(self):
        print(f'name : {self.name} species : {self.species}')

class Sound:
    def sound(self, animalName):
        print(f'{animalName} is making sound')



#           \/      \/      #inheriting the class from here
class Dog(Animal, Sound):  
    def walktime(self):
        print('walk time ! 🐕‍🦺')


dog = Dog('Shibu', 'Dog')
dog.sound(dog.name)
dog.walktime()


