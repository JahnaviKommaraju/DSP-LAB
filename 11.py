class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

def print_dll(t):
    print('The elements in the list are:')
    while(t):
        print(t.data)
        t = t.next
head=None
choice='y'
while choice=='y':
    val=int(input("Enter a number: "))
    if head==None:
        n=head=Node(val)
    else:
        t=n
        n.next=Node(val)
        n=n.next
        n.prev=t
    choice=input("Want to create another node?(y/n): ")
tail=n

print_dll(head)