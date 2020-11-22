#without function
n=int(input('Enter number'))
f=1
for i in range(1,n+1):
    f=f*i
print(f)    


# using function
def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        f=1
        for i in range(1,n-1):
            f=f*i
        return f 
n=int(input('Enter number'))
print(fact(n))

#using recursive
# def fact(n):
#     if n<0:
#         return 0
#     elif n==0 or n==1:
#         return 1
#     else:
#          n*fact(n-1)
# n=int(input('Enter number'))
# print(fact(n))         


            

