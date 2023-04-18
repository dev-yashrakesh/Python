class Fraction:
    def __init__(self,num=0,deno=1):
        if deno==0:
            deno=1
        self.num=num
        self.deno=deno

    def print(self):
        if self.num==0:
            print(0)
        elif self.deno==1:
            print(self.num)
        else:
            print(self.num,"/",self.deno)

    def simplify(self):
        if self.num==0:
            self.deno=1
            return

        current=min(self.num,self.deno)
        while current>1:
            if self.num % current==0 and self.deno % current==0:
                break
            current-=1
        self.num=self.num//current
        self.deno=self.deno//current

    def add(self,OtherFraction):
        newNum=self.num*OtherFraction.deno + self.deno*OtherFraction.num
        newdeno=self.deno*OtherFraction.deno

        self.num=newNum
        self.deno=newdeno
        self.simplify

    def multiply(self,OtherFraction):
        newnum=self.num*OtherFraction.num
        newdeno=self.deno*OtherFraction.deno

        self.num=newnum
        self.deno=newdeno
        self.simplify()

f1=Fraction(2,4)
print(f1.print())

f1.simplify()
print(f1.print())

f2=Fraction(3,5)
f1.add(f2)
print(f1.print())

f1.multiply(f2)
print(f1.print())