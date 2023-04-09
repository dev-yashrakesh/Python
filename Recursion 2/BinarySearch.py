def binarysearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2

    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return binarysearch(a,x,si,mid-1)
    else:
        return binarysearch(a,x,mid+1,ei)
x=int(input("Enter the no. u want to find"))
print(binarysearch([1,2,3,4,5,6,7,8,9,12,15,17,18,20],x,0,14))
