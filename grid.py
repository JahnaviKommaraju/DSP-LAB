#hack101


n = int(input())
cross = []
row = ''
for i in range(n):
    l = input().split()
    cross.append(l)
    row += ''.join(l)
col = ''
l2 = list(zip(*cross))
for i in l2:
    col += ''.join(i)

found = False
for i in range(int(input())):
    s = input()
    if (s==s[::-1] and (s in row or s in col)):
        found = True
        print(s)
if not found:
    print(-1)
