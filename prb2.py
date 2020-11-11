import math
n=int(input("dati numarul natural nenegativ n="))
s=0
for i in range (1,n+1):
    s+=(math.factorial(i))
print("suma 1!+2!+...n!= ",s)