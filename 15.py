class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

def print_list(t):
    c=1
    while(t!=None):
        c+=1
        t=t.next
    print('The number of elemnts in the list are:',c-1)
def print_dll(t):
    print('The DLL contains :')
    while(t):
        print(t.data)
        t = t.next
def Reverse(t):
    temp = head
    c = 0
    while temp is not None:
        c += 1
        temp = temp.next
    
    for i in range(c-1,0,-1):
        c1 = 0
        temp = head
        while (c1!= i):
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next
            c1 += 1

head = None
num=int(input('No. of elements: '))
for i in range(num):
    x=int(input('Enter element: '))
    if head == None:
        head=n=Node(x)
    else:
        n.next = Node(x)
        n = n.next
print_list(head)
print_dll(head)
Reverse(head)
print_dll(head)