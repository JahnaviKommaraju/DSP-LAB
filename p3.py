# Reverse the array with using loops
n=int(input('Enter no. of elements: '))
l=[]
for i in range(n):
    l.append(int(input('enter element: ')))
fe=0
le=n-1
t=0
while fe<le:
    t=l[fe]
    l[fe]=l[le]
    l[le]=t
    fe+=1
    le-=1
print(l)