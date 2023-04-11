class Fraction:
    def __init__(self,num=0,deno=1):
        self.num=num
        self.deno=deno

f1=Fraction(2,3)
print(f1.__dict__)

f2=Fraction()
print(f2.__dict__)

f3=Fraction(3)
print(f3.__dict__)