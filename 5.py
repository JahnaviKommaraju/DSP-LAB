# 5. count the number of nodes in the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_list(t):
    c=1
    while(t!=None):
        c+=1
        t=t.next
    print('The number of elemnts in the list are:',c-1)


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