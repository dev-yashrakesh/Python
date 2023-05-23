class Point:

    def __int__(self,x,y):
        self.__x=x
        self.__y=y

    def __str__(self):
        return "This point is at (" + str(self.__x) + "," + str(self.__y) + ")"

    def __add__(self, point_object):
        return Point(self.__x + point_object.__x, self.__y + point_object.__y)

p1=Point(1,2)
p2=Point(5,6)

p3=p1+p2
print(p3)