n=int(input())
l=[]
if(n>=2):
    for i in range(2,n):
        if(n%i==0):
            continue
        else:
            l.append(i)

print(l)