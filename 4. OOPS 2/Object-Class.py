class Circle(object):

    def __init__(self,radius):
        self.radius=radius

    def __str__(self):
        return "This is a circle class which takes the argument"

c=Circle(3)
print(c)