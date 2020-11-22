# 9. Delete a node in SLL basing on the position of the node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_list(t):
    print('The SLL contains :')
    while(t):
        print(t.data)
        t = t.next
def del_pos(t) :
    pos=int(input("enter the position"))
    count=1
    while(count<pos) :
        n=t
        t=t.next
        count=count+1
    n.next=t.next
    print("the element deleted",t.data)
    del t  
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
del_pos(head) 
print_list(head)