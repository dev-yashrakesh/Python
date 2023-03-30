def first_n(n):
    if n==0:
        return
    print(n)
    first_n(n-1)
n=int(input("Enter a number"))
print(first_n(n))