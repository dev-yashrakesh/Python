class vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.__maxSpeed=maxSpeed

    def getMaxSpeed(self):
        return self.__maxSpeed

    def setMaxSpeed(self,maxSpeed):
        maxSpeed=self.__maxSpeed

    def print(self):
        print("Color", self.color)
        print("Maxspeed", self.__maxSpeed)

class car(vehicle):
    def __init__(self,color,maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)
        self.numGears=numGears
        self.isConvertible=isConvertible

    def print(self):
        #super().print()
        print("NumGears", self.numGears)
        print("isConvertible", self.isConvertible)

c=car("Blue",175,6,True)
print(c.print())

v=vehicle("red",132)
print(v.print())