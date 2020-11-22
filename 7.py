# 7. create a SLL list in reverse order i.e store None 
# in the first node and let the second node have the
#  address of the first node.  store the address of the last node in header node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(t):
    print('The SLL contains :')
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
n=int(input('No. of elements: '))
for i in range(n):
    x=int(input('Enter element: '))
    if head == None:
        head=n=Node(x)
    else:
        n.next = Node(x)
        n = n.next
print("Given Linked List")
print_list(head)
reverse(head)
print("Reversed Linked List")
print_list(head)