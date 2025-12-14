import sys
input = sys.stdin.readline

def bt(x):
    results.append(x)
    for i in range(x%10):
        bt(x*10+i)

n = int(input())
results = []
for i in range(10):
    bt(i)
results.sort()
print(results[n] if n < len(results) else -1)