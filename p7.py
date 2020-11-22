# Move all the negative elements to one side of the array 
n=int(input('Enter no. of elements: '))
l=[]
for i in range(n):
    l.append(int(input('enter element: ')))
for i in range(0,len(l)):
    for j in range(i,len(l)) :
        if l[i]>l[j]:
           t=l[i]
           l[i]=l[j]
           l[j]=t
print(l)