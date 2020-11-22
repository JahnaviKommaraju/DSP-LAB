#prgrm to implement queue using list
class Queue:
    def __init__(self):
        self.q=[]
        self.front=0
        self.rear=0
    
    def enqueue(self,n):
        self.q.append(n)
        self.rear+=1
    
    def is_empty(self):
        if len(self,q)==0:
            return True
    
    def dequeue(self):
        if self.is_empty():
            print('Queue underflow')
        else:
            print('deleted elemnt is: ')
            print(self.q.pop(0))
    def q_len(self):
        return len(self.q)
    def
        