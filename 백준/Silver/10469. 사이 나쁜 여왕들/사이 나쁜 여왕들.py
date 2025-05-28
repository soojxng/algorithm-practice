r = set()
c = set()
v1 = set()
v2 = set()

for i in range(8):
    tmp = input().rstrip()
    for j in range(8):
        if tmp[j] == '*':
            r.add(i)
            c.add(j)
            v1.add(j - i)
            v2.add(j + i)
            
if len(r) == len(c) == len(v1) == len(v2) == 8:
    print('valid')
else:
    print('invalid')