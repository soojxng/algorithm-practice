import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
def makeStar(i):
    if i == 3:
        return ['  *  ', ' * * ', '*****']
 
    arr = makeStar(i//2)
    tmp = []
    for a in arr:
        tmp.append(' '*(i//2) + a + ' '*(i//2))
 
    for a in arr:
        tmp.append(a + ' ' + a)
 
    return tmp

n = int(input())
result = makeStar(n)
for r in result:
    print(r)