def gsum(n):
    if n==0:
        return 1
    s=1/2**n
    r=gsum(n-1)
    num=s+r
    return num
n=int(input("Enter the no."))
print(gsum(n))
