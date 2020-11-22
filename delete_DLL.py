# program for delete an element in a dll
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
# function for printing the elements in the DLL
def print_dll(t):
    print('The values in the Dll are : ')
    while(t!=None):
        print(t.data)
        t=t.next
# delete the head node
def del_head():
    global head
    t=head
    print('The deleted element is',head.data)
    head=head.next
    head.prev=None
    del t
# deleting the last node in the list
def del_tail():
    global tail
    t=tail
    print('The deleted element is',tail.data)
    tail=tail.prev
    tail.next=None
    del t
# deleting the node inbetween any two existing nodes
def del_pos(t):
    # move until we reach the pos-1 node
    counter=1
    pos=int(input('enter the position of the node to be deleted'))
    while(counter<pos):
        counter+=1
        n=t
        t=t.next
    n.next=t.next
    t.next.prev=n
    print('The deleted element is',head.data)
    del t


head=None
choice='y'
while(choice=='y'):
    val=int(input('Enter a number'))
    if head==None:
        n=head=Node(val)
    else:
        t=n
        n.next=Node(val)
        n=n.next
        n.prev=t
    choice=input('want to create another node y/n')

print('The actual list')
print_dll(head)
del_head()
# del_pos(head)
# print('The modified list after deletion is')
print_dll(head)
del_tail()
print_dll(head)



# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None

# def print_dll(t):
#     print('The elements in the DLL are:')
#     while(t!=None):
#         print(t.data)
#         t=t.next

# head =None
# choice='y'
# while(choice=='y'):
#     val=int(input('Enter an number' ))
#     if head==None:
#         n=head=Node(val)
#     else:
#         t=next.n=Node(val)
#         n.next=Node(val)
#     choice=input('want to create another node y/n')
# print_dll(head)
