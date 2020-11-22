#node creation os SLL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# function for print the nodes in a SLL

def print_list(t):
    print('The lemenets in the list are:')
    while(t):
        print(t.data)
        t=t.next

# Deleting the last node of an SLL
def del_last(t):
    # traverse the list until you reach the last but one node
    while(t.next!=None):
        n=t
        t=t.next
    print('The deleted node or value is :',t.data)
    del t
    n.next=None
    
# deleting the first ode in the SLL
def del_first(t):
    global head
    head = head.next
    del t
    
    
# deleting a node inbetween any two existing nodes
def del_inbetween(t):
    # traverse the list until you reach pos-1 location
    # accept the poistion of the node to be deleted
    pos=int(input('enter the position of the node to be deleted'))
    count=1
    while(count<pos):
       n=t
       t=t.next
       count+=1
    # connect the previous node of the node to be deleted with the 
    # next node of the node to be deleted
    n.next=t.next
    print(' the deleted element is',t.data)
    del t
# code for creating a SLL
head=None
for i in range(1,5):
    if head==None:
        head=Node(i)
        n=head
    else:
        n.next=Node(i)
        n=n.next

print_list(head)
del_last(head)
print('After deleting the last node')
print_list(head)
print('After deleting the first node')
del_first(head)
print_list(head)
del_inbetween(head)
print_list(head)









# class Node:
#     def __init__(self, data):
#             self.data = data
#             self.next = None
# #function to print 
# def print_list(t):
#     print('The SLL contains :')
#     while(t):
#         print(t.data)
#         t = t.next

# def del_last(t):
#     while(t.next!=None):
#         n=t
#         t=t.next
#     print("The deleted node or value is ",t.data)
#     del t
#     n.next=None

# def del_first(t):
#     global head
#     head=head.next
#     del t

# def del_inbetween(t):
#     #traverse the list until you reach pos-1 location
#     #accept the position of the node to be deleted
#     pos=int(input('enter position of node'))
#     c=1
#     n=t
#     while(c<pos):
#         n=t
#         t=t.next
#         c+=1
#     #connect the previous node 
#     n.next=t.next
#     print("the del elemnet ",t.data)
#     del t

# head = None

# for i in range(1,5):
#     if head == None:
#         head = Node(i)
#         n=head
#     else:
#         n.next = Node(i)
#         n = n.next
# print_list(head)
# # del_last(head)
# # print('After deletion at last')
# # print_list(head)
# # del_first(head)
# # print('After deletion at first')
# # print_list(head)

# del_inbetween(head)
# print('After deletion at given pos')
# print_list(head)
