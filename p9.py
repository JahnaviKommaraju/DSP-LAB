# cyclic rotation
n=int(input('Enter no. of elements: '))
d=int(input('Enter no. of rotations: '))
l=[]
for i in range(n):
    l.append(int(input('enter element: ')))
for i in range(d):
    t=l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
        
    l[j+1]=t
for i in l:
    print(i,end=' ')

    