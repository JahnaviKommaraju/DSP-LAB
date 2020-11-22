class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_list(t):
    print('The SLL contains :')
    while(t):
        print(t.data)
        t = t.next
def del_last(t):
    #traverse the list until you reach the last but one node
    while(t.next!=None):
        n=t
        t=t.next
    print("the deletedc valve is :",t.data)
    n.next=None
def  del_frist(t)   :
    global head
    head=head.next
    del t
def del_inbetween(t) :
    #traverse the list until you reac pos-1
    # accept the pos
    pos=int(input("enter the position"))
    count=1
    while(count<pos) :
        n=t
        t=t.next
        count=count+1
    #connect the previous node  of the node to be deleted
    # next 
    n.next=t.next
    print("the element deleted",t.data)
    del t  
head = None    
n=int(input("enter the number of element"))     
for i in range(n):
    x=int(input('Enter elements: '))
    if head == None:
        head=n=Node(x)
    else:
        n.next = Node(x)
        n = n.next
key=int(input("enter the key valve"))        
print_list(head)
if(key==n):
    del_last(head)
    print_list(head)
if(key==0):
 
    del_frist(head)
    print_list(head)
if(key!=0 and key!=n)  :
 
    del_inbetween(head) 
    print_list(head)