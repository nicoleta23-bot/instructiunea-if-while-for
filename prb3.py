m=int(input("dati numarul natural m= "))
n=int(input("dati numarul natural n="))
if (n<m):
    print("m trebuie sa fie mai mare decit n")
else:
    for i in range(1,n+1):
            if(m**i==n):
                print(n, "este putere a lui ",m)
            else:
                print(n, "nu este putere a lui", m)