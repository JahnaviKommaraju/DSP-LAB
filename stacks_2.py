# program for implementing  a stack using a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    # function for inserting or pushing an element into stack
    def push(self,elt):
        if self.top==None:
            self.top=Node(elt)
        else:
            n=Node(elt)
            n.next=self.top
            self.top=n
            
   # function is to find whether the stack is empty or not
    def is_empty(self):
        if self.top==None:
            return True
    
     # function for deleting or poping an element from stack
    def Pop(self):
        if (self.is_empty()):
            print('Stack underflow')
        else:
            print('The deleted element from the stack is', self.top.data)
            t=self.top
            self.top=self.top.next
            del t

#driver code 
s=Stack() 
s.push(555) 
s.push(20) 
s.push(339) 
s.push(44) 
# delete elt. from stack
s.Pop()
s.Pop()
#s.Pop()
#s.Pop()
s.Pop()