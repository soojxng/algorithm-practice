import sys
input = sys.stdin.readline

n = int(input())
circle = [int(input()) for _ in range(n)]
results = [0] * n

if n % 3 == 0:
    for i in range(3):
        min_val = float('inf')
        tmp = 0
        for j in range(i, n, 3):
            results[j] = tmp
            min_val = min(min_val, tmp)
            tmp += circle[(j+2) % n] - circle[(j+1) % n]

        x = (1 - min_val) if i < 2 else (circle[1] - sum(results[:3]))
        for j in range(i, n, 3):
            results[j] += x

else:
    j = 0
    tmp = 0
    for i in range(n):
        results[j] = tmp
        tmp += circle[(j+2) % n] - circle[(j+1) % n]
        j = (j+3) % n

    x = ((sum(circle) // 3) - sum(results)) // n
    results = [a+x for a in results]

for a in results:
    print(a)