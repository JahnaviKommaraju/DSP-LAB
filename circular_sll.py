# program for creating a circularly single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# code for creating a Circular SLL
head=None
for i in range(5):
    if head==None:
        n=head=Node(i)
    else:
        n.next=Node(i)
        n=n.next
# hold the address of header node in the next portion of tail node
n.next=head

# print the elements in the csll
print('The lement in the Circularly linked list are:')
n=head
print(n.data)
n=n.next
while(n!=head):
    print(n.data)
    n=n.next
