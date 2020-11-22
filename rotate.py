d=int(input())
l=[int(i) for i in input().split(' ')]
for i in range(d):
    t=l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
        
    l[j+1]=t
for i in l:
    print(l[i],end=' ')        
