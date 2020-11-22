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
