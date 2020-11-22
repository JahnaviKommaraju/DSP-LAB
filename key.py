key=int(input('enter key: '))
distance=int(input('enterdistance: '))
print('ENter elements: ')
l=[int(i) for i in input().split(' ')]
s=set(l)
a=list(s)
for i in range(len(a)-1):
    if((key-distance==a[i]) or (key+distance==a[i])):
        print(a[i])
