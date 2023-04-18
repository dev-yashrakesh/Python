def first_n(n):
    if n==0:
        return
    first_n(n-1)
    print(n)
n=int(input("Enter a number"))
print(first_n(n))