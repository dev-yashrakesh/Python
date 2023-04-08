def LastIndex(a,x):
    l=len(a)

    if l==0:
        return -1
    smallerlist=a[1:]
    smallerlistoutput=LastIndex(smallerlist,x)
    if smallerlistoutput!=-1:
        return smallerlistoutput+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

a=[1,2,3,4,5,6,7,4,2,4,9,2]
x=int(input("enter the number u want to find"))
print(LastIndex(a,x))