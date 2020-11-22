#nth term in fibanaaci

#using loops n without recursion
n=int(input('Enter n: '))
f1,f2,f=0,1,0
for i in range(n):
    f=f1+f2
    f1=f2
    f2=f
print(f)         



