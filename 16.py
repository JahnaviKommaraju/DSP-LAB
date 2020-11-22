class Student:
    def __init__(self, rno, name, branch):
        self.prev=None
        self.rno = rno
        self.name = name
        self.branch = branch
        self.next = None

def print_list(t):
    print('The Student Details are :')
    while(t):
        print(' Roll Number :',t.rno, 'Name :', t.name, 'Branch: ',t.branch)
        t = t.next


head = None
num=int(input('No. of students: '))
for i in range(num):
    r = int(input('Enter Roll Number : '))
    n = input('Enter Name : ')
    m=input("Enter branch: ")
    if head == None:
        head = s = Student(r, n, m)
    else:
        t=n
        s.next = Student(r, n, m)
        s = s.next
        s.prev=t
print_list(head)