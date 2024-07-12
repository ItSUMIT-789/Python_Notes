from abc import ABC, abstractmethod

# Abstract methods are those types of methods that don't require implementation for
#    its declaration.

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class TwoWheeler(Vehicle):
    def __init__(self, name, year, test):
        pass

    def start_engine(self):
        # code calculate 
        pass


class FourWheeler(Vehicle):
    def __init__(self, name, year):
        pass

    def start_engine(self):
        # car calculate code starting time
        pass


entry = TwoWheeler('Pulsar', '2021', 'test')
entry.start_engine()

fentry = FourWheeler('Ferrari', '2024')
fentry.start_engine()






