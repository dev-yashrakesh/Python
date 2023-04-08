def firstindex(a,x,si):
    l=len(a)

    if si==l:
        return -1
    if a[si]==x:
        return si

    smallerlistoutput=firstindex(a,x,si+1)
    return smallerlistoutput

a=[1,2,3,4,5,6,7,8,9,10]
x=int(input("Enter a no. u want to find"))
print(firstindex(a,x,0))