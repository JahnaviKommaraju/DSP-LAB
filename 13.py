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
def length(t):
    c=0
    while(t):
        t=t.next
        c=c+1
    return c

def insert_at_end(t):
    x = int(input(" number"))
    n=Node(x)
    while(t.next != None):
        t = t.next
    t.next = n
    n.next = None
  
def insert_at_pos(t,p):
    # create anew node
    x = int(input('Enter a number'))
    n = Node(x)
    pos = p
    c = 1
    while(c < pos):
        t = t.next
        c += 1
    n.next = t.next
    t.next = n

def insert_num(t):
    k=int(input("enter key"))
    l=length(t)
    if k<=l:
        insert_at_pos(t,k)
    else:
        insert_at_end(t)

head = None
s=int(input("enter size of list"))
print("enter elements")
for i in range(s):
    e=int(input())
    if head == None:
        head=Node(e)
        n=head
    else:
        t=n
        n.next=Node(e)
        n=n.next
        n.prev=t

insert_num(head)
print_list(head)