n=int(input("Introdu numărul: "))
s1a=0
s1b=0
s2a=0
s2b=0
s2=0
s1=0
s2i=0
for i in range(1,n+1):
    s1a+=i**3
for i in range(1,n+1):
    s2+=i
s2a=s2**2
if s1a>s2a:
    print("a)S1>S2")
elif s1a<s2a:
    print("a)S1<S2")
else:
    print("a)S1=S2")
for i in range(1,n+1):
    s1+=i**2
s1b=s1*3
for i in range(1,n+1):
    s2i+=i
s2b=s2i+n**3+n**2
if s1b>s2b:
    print("b)S1>S2")
elif s1b<s2b:
    print("b)S1<S2")
else:
    print("b)S1=S2")