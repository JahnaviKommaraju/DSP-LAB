key=int(input())
l=[int(i) for i in input().split(" ") ]
n=len(l)
low,high=l[0],l[n-1]
while(low<=high):
    mid=(low+high)//2
    if l[mid]==key:
        print(mid)
        break
    elif mid<key:
        low=mid+1
    elif mid:
        high=mid-1
    else:
        print('not found')
        break    









