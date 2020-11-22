# program for reversing dll using adresses

# node creation of an DLL
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

def print_dll(t):
    print('The values in the Dll are : ')
    while(t!=None):
        print(t.data)
        t=t.next


def reverse_dll(t):
    global head
    x=t
    y=None
    while(x!=None):
        n=x.next
        x.next=y
        y=x
        x=n
        head=y


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
reverse_dll(head)
print_dll(head)