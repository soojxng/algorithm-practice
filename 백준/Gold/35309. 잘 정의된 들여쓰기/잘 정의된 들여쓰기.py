import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    f = 1
    for x in a:
        if x == s[-1] + 1:
            s[-1] += 1
        elif x == 1:
            s.append(1)
        else:
            while s:
                if x == s[-1] + 1:
                    s[-1] += 1
                    break
                s.pop()
            if len(s) == 0:
                f = 0
                break
    print("YES" if f else "NO")