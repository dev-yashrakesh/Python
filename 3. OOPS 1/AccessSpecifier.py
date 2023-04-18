class student:
    passingpercentage=40
    def __init__(self,name,age=15,percentage=80):
        self.__name=name
        self.age=age
        self.percentage=percentage

    def studentDetails(self):
        print("Name=",self.__name)
        print("Age=", self.age)
        print("Percenatge=", self.percentage)
        pass

    def isPassed(self):
        if self.percenatge>student.passingpercentage:
            print("Pass")
        else:
            print("Fail")

    @staticmethod
    def welcomeToSchool():
        print("HEY!Welcome to school")

s1=student("Yash")
print(s1.studentDetails())
print(s1._student__name)