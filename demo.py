# class Topten:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         val=self.num
#         self.num+=1
#         return val
# values=Topten()
# print(next(values))        

def top():
    n=1
    while(n<=10):
        yield n
        n+=1
values=top()
for i in values:
    print(i)      