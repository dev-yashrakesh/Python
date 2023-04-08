def lastindex(a,x,si):
    l=len(a)

    if si==l:
        return-1
    smallerlistoutput=lastindex(a,x,si+1)
    if smallerlistoutput!=-1:
        return smallerlistoutput

    else:
        if a[si]==x:
            return si
        else:
            return -1

a=[1,2,3,4,5,6,4,3,5,2,5,8,1,3]
x=int(input("Enter a number u want to find"))
print(lastindex(a,x,0))