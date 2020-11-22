# key=int(input())
# l=[int(i) for i in input().split(' ')]
# pos=0
# for i in range(l):
#     for j in range(len(l)-1):
#         if(l[i]>l[j]):
#             pos=j
#             break
# for i in range(l):
#     for j in range(len(l)-1):
#         if(l[i]>l[j]):
#             pos=j
#             break
# 
arr=[17,18,5,4,6,1]
for i in range(len(arr)-1):
    max=arr[i+1]
    for j in range(i+1,len(arr)-1):
        if arr[j]>max:
            max=arr[j]
            print('max at',j,'is',max)
    arr[i]=max
arr[len(arr)-1]=-1     
print(arr)  