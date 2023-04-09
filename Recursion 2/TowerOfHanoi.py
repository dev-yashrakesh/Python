def towerhanoi(n,a,b,c):
    if n==1:
        print("move 1st disk from", a, "to", c)
        return
    towerhanoi(n-1,a,c,b)
    print("move",n,"th disk from",a,"to",c)
    towerhanoi(n-1,b,a,c)

n=int(input("Enter the no. of disk"))
print(towerhanoi(n,"a","b","c"))