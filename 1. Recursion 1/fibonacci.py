def fib(n):
    if n==1 or n==2:
        return 1
    num=fib(n-1)+fib(n-2)
    return num
n=int(input("Enter a number"))
print(fib(n))