# program for count number of nodes

# node creation of an DLL
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        # function for print the nodes in a SLL
def print_forward_list(t):
    c=1
    while(t!=None):
        c+=1
        t=t.next
    print('The number pf elemnts in the list are:',c)



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