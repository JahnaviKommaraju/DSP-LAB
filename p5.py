# #  Find the "Kth" max and min element of an array 
k=(int(input ("enter kth element")))
n=int(input('Enter no. of elements: '))
l=[]
for i in range(n):
    l.append(int(input('enter element: ')))
t=0
for i in range(0,len(l)):
    for j in range(i,len(l)-1) :
        if l[i]>l[j]:
           t=l[i]
           l[i]=l[j]
           l[j]=t
print(l[k])  
fe=0
le=n-1
t=0
while fe<le:
    t=l[fe]
    l[fe]=l[le]
    l[le]=t
    fe+=1
    le-=1
print(l[k])
















# def findKthLargest(nums,k):
# 	if (k < 1 or nums == null) :
# 		return 0
 
# 	return getKth(nums.length - k +1, nums, 0, nums.length - 1)
 
# def getKth(k,nums,start, end):
 
# 	pivot = nums[end]
 
# 	left = start
# 	right = end
 
# 	while (true):
 
# 		while (nums[left] < pivot and left < right):
# 			left+=1
 
# 		while (nums[right] >= pivot and right > left):
# 			right-=1;
 
# 		if (left == right):
# 			break;
 
# 		def swap(nums, left, right)
 
#     def swap(nums, left, end)
 
# 	if(k == left + 1):
# 		return pivot
# 	elif (k < left + 1):  
# 		return getKth(k, nums, start, left - 1)
# 	else:
# 		return getKth(k, nums, left + 1, end)
# def swap(nums,n1,n2):
# 	tmp = nums[n1]
# 	nums[n1] = nums[n2]
# 	nums[n2] = tmp