# program for creating a DLL and displaying it

# node creation of an DLL
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        # function for print the nodes in a SLL
def print_forward_list(t):
    print('The elements in the list are:')
    while(t):
        print(t.data)
        t=t.next
def print_backward_list(t):
    print('The elements in the list in reverse order are:')
    while(t):print(t.data)
    t=t.prev
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
print_forward_list(head)
print_backward_list(tail)