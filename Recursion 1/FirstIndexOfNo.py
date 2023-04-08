def FirstIndex(a,x):
    l=len(a)
    if l==0:
        return -1

    if a[0]==x:
        return 0

    smallerlist=a[1:]
    smallerlistoutput=FirstIndex(smallerlist,x)

    if smallerlistoutput==-1:
        return -1
    else:
        return smallerlistoutput+1

a=[1,2,3,4,5,6,7,8]
x=int(input("Enter the number u want to find"))
print(FirstIndex(a,x))
