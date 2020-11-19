n=int(input("dati virsta lui Mihai: "))
nb=1
if ((n<=20) or (n>=0)):
    for i in range(1,n+1):
        if (i==1):
            nb=nb+2
        else:
            nb=(nb*2)+i
if ((n>20) or (n<1)): 
    print("calculam suma de la 1 an pina la 20 de ani!!")


print("mihai a primit " , nb, "dolari")
print("suma primita de Mihai trece de 100 dolari de la 6 ani")