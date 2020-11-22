# Insertion in Circularly linked SLL basing on key value
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_csll(t):
    print('The element in the Circularly linked list are:')
    n=head
    print(n.data)
    n=n.next
    while(n!=head):
        print(n.data)
        n=n.next

def insert_at_pos(t):
    # create a new node
    x = int(input('Enter a number'))
    n = Node(x)
    pos = int(input('Enter the position where to insert'))
    # move the variable t to position -1 location
    c = 1
    while(c < pos):
        t = t.next
        c += 1
    # link the new node to the existing list
    n.next = t.next
    t.next = n


# code for creating a Circular SLL

head = None
num=int(input('No. of elements: '))
for i in range(num):
    x=int(input('Enter element: '))
    if head==None:
        n=head=Node(x)
    else:
        n.next=Node(x)
        n=n.next
# hold the address of header node in the next portion of tail node
n.next=head

# print the elements in the csll
print('before insertion')
print_csll(head)
insert_at_pos(head)
print('after insertion')
print_csll(head)
