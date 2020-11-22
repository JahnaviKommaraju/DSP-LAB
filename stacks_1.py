#stacks using arrays
class Stack:   
    def __init__(self):        
        self.stack =[]         
        self.top=-1   
          # function for inserting or pushing an element into stack     
    def push(self,elt):         
        self.top+=1 
        self.stack.append(elt)     
               # function is to find whether the stack is empty or not     
    def is_empty(self):         
        if (len(self.stack))==0:             
            return True    
                   # function for deleting or poping an element from stack
    def Pop(self):
        if (self.is_empty()):             
            print('Stack underflow')        
        else:             
            print('The deleted element from the stack is', self.stack.pop())       
            self.top-=1              
                 # function for printing the elements in the stack    
    def display(self):         
        if (self.is_empty()):
            print('Stack is empty')         
        else:             
            print('The elements in the stack ')             
            for i in range(self.top,-1, -1):                 
                print(self.stack[i])


#driver code 
s=Stack() 
s.push(555) 
s.push(20) 
s.push(339) 
s.push(44) 
# delete elt. from stack
s.Pop()
s.Pop()
s.display()
#s.Pop()
#s.Pop()
s.display()
s.Pop()