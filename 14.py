# # 14. Reverse the elements of the linked list

#     #   a. By swapping the values in the list without changing the links
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

def print_list(t):
    print('The elements in the list are:')
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
         head=Node(x)
         n=head
    else:
        t=n
        n.next=Node(x)
        n=n.next
        n.prev=t
print_list(head)
Reverse(head)
print_list(head)


#   b. By swapping the position of the nodes

class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

def print_list(t):
    print('The elements in the list are:')
    while(t):
        print(t.data)
        t = t.next
def reverse(t):
    global head
    x= None
    y = head
    while( y!=None):
        next = y.next
        y.next = x
        x = y
        y = next
        head = x   

head = None
num=int(input('No. of elements: '))
for i in range(num):
    x=int(input('Enter element: '))
    if head == None:
         head=Node(x)
         n=head
    else:
        t=n
        n.next=Node(x)
        n=n.next
        n.prev=t
print_list(head)
reverse(head)   
print_list(head)