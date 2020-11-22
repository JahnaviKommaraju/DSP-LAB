# program for creating a DLL and displaying it

# node creation of an DLL
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

# function for print the nodes in a DLL in dorward direction

def print_forward_list(t):
    print('The elements in the list are:')
    while(t):
        print(t.data)
        t=t.next
# function for print the nodes in backward direction in a DLL
def print_backward_list(t):
    print('The elements in the list in reverse order are:')
    while(t):
        print(t.data)
        t=t.prev
    
def insert_beg():
    n=Node(11) # creates a new node n with 11 in its data part
    global head
    n.next=head
    n.prev=None
    head.prev=n
    head=head.prev
# function for inserting at the end a DLL
def insert_end():
    global tail
    # accept the data you want to store in the new node
    x=int(input('Enter a number'))
    n=Node(x) # creates a new node n with x in its data part
    # linking the new node at end
    tail.next=n
    n.prev=tail
    n.next=None
    tail=tail.next
    
# function for inserting  a new node at a given position
def insert_pos(t):
    # accept the data you want to store in the new node
    x=int(input('Enter a number'))
    n=Node(x) # creates a new node n with x in its data part
    pos=int(input('Enter the position of the node to be inserted'))
    # move until pos-1 location
    counter=1
    while(counter<pos):
        t=t.next
        counter+=1
    
    # linking the new node at end
    n.prev=t
    n.next=t.next
    t.next=n
    t=n.next
    t.prev=n
    
# code for creating a DLL
head=None
for i in range(1,5):
    if head==None:
        head=Node(i)
        n=head
    else:
        t=n
        n.next=Node(i)
        n=n.next
        n.prev=t
tail=n       

# insert_beg()
# insert_end()
insert_pos(head)
print_forward_list(head)
# print_backward_list(tail)

