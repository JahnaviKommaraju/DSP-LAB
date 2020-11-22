# l=[int(i) for i in input().split(' ')]
# for i in l:
#     print(i,end=' ')

# l=list(map(int,input().split()))
# for i in range(1,len(l)):
# #   for j in range(i):
# #  """    if l[i]<l[j]:
# #     #   l.insert(j,l[i])
# #     #   l.pop(i+1) """
#         key=l[i]
#       break
# print(l)

# for i in l:
#     j=l.index(i)
#     while j>0:
#         if l[j-1]>l[j]:
#             l[j-1],l[j]=l[j],l[j-1]
#         else:
#             break
#         j-=1
# print(l) 

# l=[int(i) for i in input('Enter the list of numbers: ').split()]
# for i in range(0,len(l)-1):
#     key=i
#     for i in range(i+1,len(l)):
#         if l[j]<l[k]:
#             key=j
#     l[i],l[key]=l[key],l[i]
# print(l) 


# n=int(input('Enter number of elments: '))
# l=[]
# for i in range(0,n):
#     l.append(int(input('Enter element: ')))
# x=int(input('Enter element to be searched: '))
# low=0
# high=n-1
# while(low<=high):
#     m=(low+high)//2
#     if(x<l[m]):
#         high=m-1
#     elif(x>l[m]):
#         low=m+1
#     else:
#         print('Element is found at',m+1,'position')
#         break
# if(low>high):
#     print('Element is not found')


# def linearsearch(arr, x):
#    for i in range(len(arr)):
#       if arr[i] == x:
#          return i
#    return -1def check(n) : 
      
    # Count the number of digits 
    l = countDigit(n) 
    dup = n; sm = 0
  
    # Calculates the sum of digits 
    # raised to power 
    while (dup) : 

# n=int(input('Enter number of elments: '))
# l=[]
# for i in range(0,n):
#     l.append(int(input('Enter element: ')))
# x=int(input('Enter element to be searched: '))
# print("element found at index ",(linearsearch(l,x)))


# def binarySearch(arr, l, r, x): 
#     while l <= r: 
#         m= l + (r - l) // 2
#         if arr[m] == x: 
#             return m  
#         elif arr[m] < x: 
#             l = m + 1
#         else: 
#             r = m - 1
#     return -1
   
# n=int(input('Enter number of elments: '))
# a=[]
# for i in range(0,n):
#     a.append(int(input('Enter element: ')))
# x=int(input('Enter element to be searched: '))
# res= binarySearch(a, 0, len(a)-1, x) 
  
# if res != -1: 
#     print ('Element is present at index',res,'pos') 
# else: 
#     print ('Element is not present in array') 

# n=int(input('Enter number of elments: '))
# a=[]
# for i in range(0,n):
#     a.append(int(input('Enter element: ')))
# print('ELements before soring are: ',a)
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         if(a[i]>a[j]):
#             a[i],a[j]=a[j],a[i]
# print('after sorting elemnts are: ',a)

def check(n) : 
    if (n == 0) : 
        return 0
 
    dup = n; sm = 0
  
    while (dup) : 
        sm = sm + pow(dup % 10, l) 
        dup = dup // 10
      
    if(n == sm):
        return True
    else:
        return False

