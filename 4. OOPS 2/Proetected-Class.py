class vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self._maxSpeed=maxSpeed

    def getMaxSpeed(self):
        return self._maxSpeed

    def setMaxSpeed(self,maxSpeed):
        maxSpeed=self._maxSpeed

    def print(self):
        print("Color", self.color)
        print("Maxspeed", self._maxSpeed)

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