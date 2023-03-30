def sum_n(n):
    if (n==0):
        return 0
    smalloutput=sum_n(n-1)
    output=n+smalloutput
    return output
n=int(input("Enter a number"))
print(sum_n(n))