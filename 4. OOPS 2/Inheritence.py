class vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.maxSpeed=maxSpeed

class car(vehicle):
    def __init__(self,color,maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)
        self.numGears=numGears
        self.isConvertible=isConvertible

    def printCar(self):
        print("Color",self.color)
        print("Maxspeed", self.maxSpeed)
        print("NumGears", self.numGears)
        print("isConvertible", self.isConvertible)

c=car("Blue",175,6,True)
print(c.printCar())
