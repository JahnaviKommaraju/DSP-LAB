# print('Enter 10 numbers')
# l=[int(i)+i for i in input().split()]
# # for i in range(len(l)):
# #     l[i]=l[i]+i
# print('Before modification: ',l,end=" ")
# print('After modification: ')
# print(l, end=" ")   
# print([int(input()) + i for i in range(10)])
# print([int(input())+i for i in range(10)])

# Accept a sentence and print reverse of each word

# l=[i[::-1] for i in input().split(" ")]
# print(str(l),end=" ")
# nums=[3,2,2,3]
# val=3
# j=len(nums)-1
# for i in range(0,j):
#     if nums[i]==val:
#         while (nums[j]!=val):
#             nums[i],nums[j]=nums[j],nums[i]
#             j-=1
#     if(i==j):
#         break
# print(i)
# print(nums)
# print(j)
# nums = [0,0,1,1,1,2,2,3,3,4]
# nums=list(set(nums))
# # c=0
# # for i in range(1,len(nums)):
# #     if(nums[c]!=nums[i]):
# #         nums[c]=nums[i]
# #         c+=1
# print(nums)
        
l=[10,2,5,3]
m=max(l)
for i in range(len(l)):
    if m==2*l[i]:
        print(True)
    else:
        print('f')



