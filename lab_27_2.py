# 6. Program to reverse all the nodes in a SLL
#    Test Case1:
#     I/P: 
#        1->2->3->4->None
#     O/P:
#        4->3->2->1->None
#    a. by swapping the values in the SLL without relocating the nodes
#    b. Shift the nodes(relocate) for reversing(modify the addresses)
#reverse sLL

#    b. Shift the nodes(relocate) for reversing(modify the addresses)
# class Node:
#     def _init_(self, data):
#         self.data = data
#         self.next = None
# def print_list(t):
#     print('The SLL contains :')
#     while(t):
#         print(t.data)
#         t = t.next        
# def reverse(t):
#     global head

#     x= None
#     y = head
#     while( y!=None):
#         next = y.next
#         y.next = x
#         x = y
#         y = next
#         head = x   
# head = None

# for i in range(10):
#     if head == None:
#         head = n = Node(i)
#     else:
#         n.next = Node(i)
#         n = n.next            
# print_list(head)
# reverse(head)   
# print_list(head)

#  a. by swapping the values in the SLL without relocating the nodes
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def print_list(t):
    print('The SLL contains :')
    while(t):
        print(t.data)
        t = t.next
    
def Reverse(t):
    temp = head
    c = 0
    while temp is not None:
        c += 1
        temp = temp.next
    
    for i in range(c-1,0,-1):
        c1 = 0
        temp = head
        while (c1!= i):
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next
            c1 += 1

head = None
num=int(input('No. of elements: '))
for i in range(num):
    x=int(input('Enter element: '))
    if head == None:
        head=n=Node(x)
    else:
        n.next = Node(x)
        n = n.next
print_list(head)
Reverse(head)
print_list(head)