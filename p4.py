#   Find the maximum and minimum element in an array
n=int(input('Enter no. of elements: '))
l=[]
for i in range(n):
    l.append(int(input('enter element: ')))
maxi=l[0]
mini=l[0]
for i in range(0,n):
    if l[i]>maxi:
        maxi=l[i]
    if l[i]<mini:
        mini=l[i]
print(maxi,' ',mini)