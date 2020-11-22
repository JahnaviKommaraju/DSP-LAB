# l=[int(i) for i in input().split()] 
# arr=[]
# for i in range(3):
#     arr.append(list(map(int, input().rstrip().split())))
# s1=0
# for i in range(3):
#     s1+=arr[i][i]
# s2=0
# for j in range(3):
#     s2+=arr[j][n-1-j]
# print(s1,' ',s2)
# # d=abs(s1-s2)
# n=4
# for i in range(n):
#     for k in range(n-i):
#         print(' ',end='')
#     for j in range(i+1):
#         print('#',end='')
#     print()   

l=[1,2,3]
l1=l
l[2]=4
print(l1)
print(l)