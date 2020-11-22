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
def search(t) :
    x=int(input("enter the element to be searched"))  
    n=head 
    c=1
    s=0
    while(n!=None) :
        if(n.data==x):
            s=1
            break
        else:
            n=n.next
            c+=1
    if s==1:
        print("element is found at position ",c)
    else:
        print('not found')
head = None
n=int(input('No. of elements: '))
for i in range(n):
    x=int(input('Enter element: '))
    if head == None:
        head=Node(x)
        n=head
    else:
        t=n
        n.next=Node(x)
        n=n.next
        n.prev=t
print_dll(head)       
search(head)