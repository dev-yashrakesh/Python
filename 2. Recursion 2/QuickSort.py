def partition(a,si,ei):
    pivot=a[si]
    c=0

    for i in range (si,ei+1):
        if a[i]<pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c

    i=si
    j=ei

    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pivot_index

def quick(a,si,ei):
    if si>=ei:
        return
    pivot_index=partition(a,si,ei)
    quick(a, si, pivot_index - 1)
    quick(a,pivot_index+1,ei)

a=[10,2,3,7,9,11,23,1,4,5,6]
quick(a,0,len(a)-1)
print(a)