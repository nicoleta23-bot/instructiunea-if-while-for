n=int(input("dati numărul= "))
for p in range(1,n):
    s=0
    for i in range(1,p):
        if (p%i==0):
            s+=i
    if s==p:
        print(p,end=" ")