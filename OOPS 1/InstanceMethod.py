class student():
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo

    def printStudent(self):
        print("My name is", self.name,"And rollno is",self.rollNo)

s1=student("Yash",205)
print(s1.__dict__)

print(s1.printStudent())
print(student.printStudent(s1))