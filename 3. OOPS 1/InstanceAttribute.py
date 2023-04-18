class student:
    pass
s1=student()
s2=student()
s3=student()

s1.name="Yash"
s2.rollno=205

s3.name="Parzival"
s3.rollno=49

print(s1.__dict__)
print(s3.__dict__)

print(hasattr(s1,"name"))
print(hasattr(s2,"name"))

print(getattr(s1,"name"))
print(getattr(s3,"rollno"))

print(delattr(s3,"rollno"))