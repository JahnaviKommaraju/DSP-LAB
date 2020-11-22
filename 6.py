class Student:
    def __init__(self, rno, name, branch):
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
    b= input('Enter branch : ')
    if head == None:
        head = s = Student(r, n, b)
    else:
        s.next = Student(r, n, b)
        s = s.next

print_list(head)