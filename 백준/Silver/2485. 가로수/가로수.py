import sys
input = sys.stdin.readline

def find(a, b):
    if a%b == 0:
        return int(b)
    else:
        return find(b, (a%b))
    
n = int(input())
l = list()
a = int(input())
ans = 0
for _ in range(n-1):
    b = int(input())
    l.append(b-a)
    a = b
li = set(l)
li = list(li)
while len(li) != 1:
    li[0] = find(li[0], li[1])
    del li[1]
for i in l:
    if i > li[0]:
        ans = ans + (i//li[0]) - 1
print(ans)