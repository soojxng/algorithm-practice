import sys
input = sys.stdin.readline

def mv():
    s = 0
    if base[2] and base[1] and base[0]:
        base[2] = 0
        s = 1
    if base[1] and base[0]:
        base[1] = 0
        base[2] = 1
    if base[0]:
        base[0] = 0
        base[1] = 1
    base[0] = 1
    return s

N = int(input())
balls = list(map(int, input().split()))

fb = 0
base = [0, 0, 0]
ans = 0
for b in balls:
    if b == 1:
        fb += 1
    if b == 2:
        fb = 0
        ans += mv()
    if b == 3:
        fb += 1
        if base[2]:
            base[2] = 0
            ans += 1
        if base[1]:
            base[1] = 0
            base[2] = 1
        if base[0]:
            base[0] = 0
            base[1] = 1
    if fb == 4:
        fb = 0
        ans += mv()
print(ans)  