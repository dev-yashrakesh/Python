def fact(n):
    if (n==0):
        return 1
    SmallOutput=fact(n-1)
    return n*SmallOutput
n=int(input("Enter a number"))
print(fact(n))
