class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=None
#creating a new node with value 2 in it as well a storing adress of that in the 
#next part of the previous node
num=int(input())
for i in range(num):
    if head==None:
        head=Node(i)
        n=head
    else:
        n.next=Node(i)
        n=n.next  

#printing nodes
n=head
while(n!=None):   
    print(n.data)
    n=n.next
