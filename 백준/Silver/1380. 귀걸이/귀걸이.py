import sys
input = sys.stdin.readline

i = 1
while 1:
    n = int(input())
    if n == 0: break
    girls = [input().strip() for _ in range(n)]
    ans = set()
    for _ in range(2*n-1):
        x, y = input().strip().split()
        if x not in ans:
            ans.add(x)
        else:
            ans.remove(x)
    for a in ans:
        print(i, girls[int(a)-1])
    i += 1