class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        
# for printing the nodes in the list
def print_list(t):
    print('The SLL contains :')
    while(t):
        print(t.data)
        t=t.next

# # insert at the begining
# def insert_at_begin(t):
#     global head
#     x = int(input('Enter a number'))
#     n = Node(x)
#     # link the new node to the already existing head node
#     n.next = t
#     # make the new node as the head node
#     head= n

# def insert_at_end(t):
#     #create a new node and get data into it
#     n=Node(33)
#     # now start linking the new node to the existing list
#     # firstly move to the last node from header node as we have only
#     # header node address in hand
#     while(t.next!=None):
#         t=t.next
#     # secondly link the existing last node and the new node
#     t.next=n
#     # Lastly make the newly inerted node as the tail/last node
#     n.next=None
#     # now the insertion process is complete


#insert at po
def insert_at_pos(t):
    # create anew node
    x = int(input('Enter a number'))
    n = Node(x)
    pos = int(input('Enter the position where to insert'))
    # move the variable t to position -1 location
    c = 1
    while(c < pos):
        t = t.next
        c += 1
    # link the new node to the existing list
    n.next = t.next
    t.next = n
# create a SLL
    
head=None

for i in range(3):
    if head == None:
        head=n= Node(i)
    else:
        n.next= Node(i)
        n=n.next

print_list(head)
# insert_at_begin(head)
# insert_at_end(head)
insert_at_pos(head)
print('printing the new list after insertion')
print_list(head)