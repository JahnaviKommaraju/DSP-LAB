# 1. Write a program to search for an element in a SLL.  (linear Search)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_list(t):
    print('The SLL contains :')
    while(t):
        print(t.data)
        t = t.next
def search(t):
    x=int(input("enter the element to be searched")) 
    c=1 
    s=0
    while(t!=None) :
        if(t.data==x):
            s=1
            break
        else:
            t=t.next
            c+=1
    if s==1:
         print("element is found at position ",c)
    else:
         print("element is not found")

head = None
n=int(input('No. of elements: '))
for i in range(n):
    x=int(input('Enter element: '))
    if head == None:
        head=n=Node(x)
    else:
        n.next = Node(x)
        n = n.next
search(head)