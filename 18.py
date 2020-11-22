
# 8. Delete a node in DLL basing on the key value
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def print_list_forward(t):
    while(t):
        print(t.data)
        t=t.next
def delete_key(t,k):
    while(t.next!=None):
        if(t.data==k):
            t.prev.next=t.next
            t.next.prev=t.prev
        t=t.next
    if t.data==k:
        t.prev.next=None


head=None
n=int(input('No. of elements: '))
for i in range(n):
    x=int(input('Enter element: '))
    if head==None:
        head=n=Node(x)
    else:
        t=n
        n.next=Node(x)
        n=n.next
        n.prev=t
tail=n

print('before deleting ')
print_list_forward(head)
x=int(input('enter the element you want to delete'))
delete_key(head,x)
print_list_forward(head)