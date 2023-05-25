from abc import ABC,abstractmethod

class Automobile(ABC):
    def __int__(self):
        print("Automobile created")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Automobile):
    def __int__(self, name):
        print("Car is created")
        self.name = name

    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass

c=Car("Honda")
print(c)