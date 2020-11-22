# 1. Implement A SLL by accepting the data to be stored into the linked list from the user
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_list(t):
    print('The SLL contains :')
    while(t):
        print(t.data)
        t = t.next
        
head = None
n=int(input('No. of elements: '))
for i in range(n):
    x=int(input('Enter element: '))
    if head == None:
        head=n=Node(x)
    else:
        n.next = Node(x)
        n = n.next
print_list(head)