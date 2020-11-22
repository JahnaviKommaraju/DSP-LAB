# 19. Delete a node in DLL basing on the position of the node
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

def del_pos(t):
    counter=1
    pos=int(input('enter the position of the node to be deleted'))
    while(counter<pos):
        counter+=1
        n=t
        t=t.next
    n.next=t.next
    t.next.prev=n
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

print_dll(head)
del_pos(head)
print('After deletion')
print_dll(head)