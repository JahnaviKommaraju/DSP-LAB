# program for sorting dll

# node creation of an DLL
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

def print_dll(t):
    print('The values in the Dll are : ')
    while(t!=None):
        print(t.data)
        t=t.next

def sort_dll(t):
    while(t!= None):   
        n = t.next;  
        while(n != None):  
            if (t.data > n.data):  
                t.data,n.data = n.data,t.data  
            n = n.next  
        t = t.next  

    # code for creating a DLL

head = None
num=int(input('No. of elements: '))
for i in range(num):
    x=int(input('Enter element: '))
    if head==None:
        head=Node(x)
        n=head
    else:
        t=n
        n.next=Node(x)
        n=n.next
        n.prev=t
        tail=n
sort_dll(head)
print_dll(head)