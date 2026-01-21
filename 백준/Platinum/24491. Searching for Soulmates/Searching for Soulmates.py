import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    li = [(a, 0)]

    x = a
    while x > 1:
        if x % 2 == 0:
            x //= 2
        else:
            x += 1
        li.append((x, len(li)))
    
    li.sort()
    ans = float('inf')
    y = b
    cnt = 0
    while y > 0:
        for x, i in li:
            if x > y:
                break
            ans = min(ans, i + cnt + y - x)

        if y % 2 == 0:
            y //= 2
        else:
            y -= 1
        cnt += 1

    print(ans)