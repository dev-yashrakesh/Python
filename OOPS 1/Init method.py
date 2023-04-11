class student():
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo

s1=student("Yash",205)
print(s1.__dict__)

s2=student("Parzival",48)
print(s2.__dict__)

s3=student("Rohan",12)
print(s3.__dict__)