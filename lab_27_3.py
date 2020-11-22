# 1. Write a program to search for an element in a SLL.  (linear Search)
#   if the  element is found print its location otherwise print 'not found'

# 2. Program to insert an element in the beginining in an SLL
# 3. Program to insert an element at the end of an SLL
# 4. Program to insert an element at a given position in a SLL

# 5. Program to insert an element after a given value in an SLL
# 6. Program to reverse all the nodes in a SLL
#    Test Case1:
#     I/P: 
#        1->2->3->4->None
#     O/P:
#        4->3->2->1->None
#    a. by swapping the values in the SLL without relocating the nodes
#    b. Shift the nodes(relocate) for reversing(modify the addresses)

# 7. Program to sort the elements in a SLL
# 8. Program to create an SLL in Reverse order
# 	None<-1<-2<-3




class Node:
    def _init_(self, data):
            self.data = data
            self.next = None

# for printing the nodes in the list
def print_list(t):
    print('The SLL contains :')
    while(t):
        print(t.data)
        t = t.next

# Insertion at end in an SLL

def insert_at_end(t):
    # create a new node and get data into it
    n = Node(33)
    # now start linking the new node to the existing list
    # firstly move to the last node from header node as we have only
    # header node address in hand
    while(t.next != None):
        t = t.next
    # secondly link the existing last node and the new node
    t.next = n
    # Lastly make the newly inerted node as the tail/last node
    n.next = None
    # now the insertion process is complete




def insert_at_begining(t):
    x = int(input('Enter a number'))
    n = Node(x)
    n.next = t
    global head
    head = n


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


# search in SLL
def search_in(t, s):
    i=0
    # s = int(input('Enter element to be searched: '))
    while(t):
        if s == t.data:
            # return 'Found At '+str(i+1)
            return i
        t = t.next
        i+=1
    # return 'Not Found'
    return -1

# insert after given value
def insert_value(t):
    # create anew node
    x = int(input('Enter a number : '))
    n = Node(x)
    val = int(input('Enter the value after which to insert : '))
    pos = search_in(t, val)
    if pos == -1:
        return
    # move the variable t to position -1 location
    c = 1
    while(c <= pos):
        t = t.next
        c += 1
    # link the new node to the existing list
    n.next = t.next
    t.next = n


def rev_values(t):
    rev = Node(t.data)
    t = t.next
    while(t):
        temp = rev
        rev = Node(t.data)
        rev.next=temp
        t = t.next
    return rev
        
# sorting SLL
def lmin(t):
    m = t.data
    t=t.next
    while(t):
        if m>t.data:
            m = t.data
        t=t.next
    return m

def lsort(t):
    pass


# length of sll
def length(t):
    c=0
    while t:
        t=t.next
        c+=1
    return c
#create a SLL
head = None

for i in range(3):
    if head == None:
        head = n = Node(i)
    else:
        n.next = Node(i)
        n = n.next

# insert_at_end(head)
# printing the new list after insertion
# insert_at_begining(head)
# insert_at_pos(head)
# print(search_in(head))
# insert_value(head)
# print_list(head)
# head = rev_values(head)
# print(length(head)) 
print_list(head)


