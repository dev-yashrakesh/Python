class ComplexNo:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def OtherNumber(self,OtherFunction):
        newreal=self.real+OtherFunction.real
        newimg=self.img+OtherFunction.real
        self.real=newreal
        self.img=newimg
        print(self.real,"+",self.img,"i")

c1=ComplexNo(2,3)
c2=ComplexNo(3,5)

c1.OtherNumber(c2)
print(c1)


