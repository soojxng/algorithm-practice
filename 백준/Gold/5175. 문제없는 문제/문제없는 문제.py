import sys
import itertools
input = sys.stdin.readline

d = dict()
a = 65
for i in range(25):
    d[i] = chr(a+i)

for k in range(1, int(input())+1):
    m, n = map(int, input().split())
    problems = [0]*n
    for i in range(n):
        tmp = 0
        for x in map(int, input().split()):
            tmp = tmp | (1 << x)
        problems[i] = tmp
    
    ans = 0
    for i in range(1, m+1):
        ans = ans | (1 << i)
        
    f = 0
    for i in range(1, n+1):
        for c in itertools.combinations(range(n), i):
            tmp = 0
            for x in c:
                tmp = tmp | problems[x]
            if tmp == ans:
                f = c
                break
        if f:
            break
    result = [d[x] for x in f]
    print(f"Data Set {k}: {' '.join(result)}")
    print()