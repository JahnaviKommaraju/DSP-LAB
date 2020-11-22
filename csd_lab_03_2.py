# program for searching an elemnet in dll

# node creation of an DLL
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        # function for print the nodes in a SLL
def search(t):
    x=int(input("enter the element to be searched")) 
    c=1 
    s=0
    while(t!=None) :
        if(t.data==x):
            # print("element is found at position ",c)
            s=1
            break
        else:
            t=t.next
            c+=1
    if s==1:
         print("element is found at position ",c)
    else:
         print("element is not found")

# code for creating a DLL
head=None
for i in range(1,5):
    if head==None:
        head=Node(i)
        n=head
    else:
        t=n
        n.next=Node(i)
        n=n.next
        n.prev=t
        tail=n
search(head)