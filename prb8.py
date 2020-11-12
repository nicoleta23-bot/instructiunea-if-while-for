a=int(input("dati primul nr: "))
b=int(input("dati al doilea nr: "))
c=int(input("dati al treilea nr: "))
if (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
    print("este triunghi")
    if ((a==b==c)):
        print("echilateral")
    if (((a==b) and (a!=c)) or ((b==c) and (b!=a)) or ((a==c) and (a!=b))):
        print("isoscel")
    if (a!=b!=c):
        print("scalen")
else:
    print("nu este asa triunghi")
