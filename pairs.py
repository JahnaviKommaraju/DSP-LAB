def pairs(l,key):
    res=[]
    for i in l:
        if i+key in l:
            res.append(tuple((i,i+key)))
    return res

key=int(input('Enter key: '))
l=[int(i) for i in input().split(' ')]
print(pairs(l,key))

