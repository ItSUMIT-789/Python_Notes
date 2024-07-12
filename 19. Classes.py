# Basic class type

class Animal:
    def __init__(self, name, species): # __init__ method and self method are compulsary
        self.name = name
        self.species = species

    def information(self):
        print(f'name : {self.name}  species : {self.species}')


dog = Animal('abc', 'xyz')
cat = Animal('pqr', 'vvv')

dog.information()
cat.information()





class Company:
    def employeesDeatails():
        pass

    def deptDetails():
        pass

    def resourcesDetails():
        pass

    def todos():
        pass


org = Company()