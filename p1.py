# Write a prgrm to find the max element of array and swap it waith last unsorted value of array.Repeat till the array is sorted
n=int(input('Enter no. of elements: '))
l=[]
for i in range(n):
    l.append(int(input('enter element: ')))
for i in range(n-1,0,-1):
    max=i
    for j in range(0,i):
        if l[j]>l[max]:
            max=j
            t=l[i]
            l[i]=l[max]
            l[max]=t

print(l)
print('max element is: ',l[n-1])