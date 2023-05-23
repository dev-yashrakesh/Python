class Mother:
    def print(self):
        print("Print of Mother called")

class Father:
    def print(self):
        print("Print of Father called")

class Child(Mother,Father):
    def __init__(self,name):
        self.name=name

    def printchild(self):
        print("Child name is ", self.name)
c=Child("Yash")
print(c.print())