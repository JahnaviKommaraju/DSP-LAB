# 3. Insert a new node basing on the key value. if key is found insert the new node after the key value.  if key value is not found add the new node at the end of the existing list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(t):
    print('The SLL contains :')
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
    x = int(input("enter new node value :"))
    n=Node(x)
    while(t.next != None):
        t = t.next
    t.next = n
    n.next = None
  
def insert_at_pos(t,p):
    x = int(input("enter new node value :"))
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
    l=find(t,k)
    if l!=False:
        insert_at_pos(t,l)
    else:
        insert_at_end(t)

head = None
s=int(input("enter size of list"))
print("enter elements")
for i in range(s):
    e=int(input())
    if head == None:
        head = n = Node(e)
    else:
        n.next = Node(e)
        n = n.next

def find(t,k):
    x=k
    c=0
    l=0
    while(t):
        if x == t.data:
            c=1
            break
        else:
            c=0
        t=t.next
        l=l+1
    if c==1:
        return l+1
    else:
        return False

insert_num(head)
print_list(head)