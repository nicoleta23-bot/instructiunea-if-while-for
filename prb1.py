n=int(input("Dati numarul natural n="))
if ((n<28) or (n>31)):
    print("nu exista asa luna")
else:
    if ((n==28) or (n==29)):
        print("februarie")
    if (n==30):
        print("aprilie, iunie, septembrie, noiembrie")
    if(n==31):
        print("ianuarie, martie, mai, iulie, august, octombrie, decembrie")
