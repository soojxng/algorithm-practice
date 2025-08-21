import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bt(can):
    if len(picnic) == k:
        for p in picnic:
            print(p)
        sys.exit(0)
    
    if len(picnic) + len(can) < k:
        return
    
    for i in range(len(can)):
        cann = [x for x in can[i+1:] if x in friend[can[i]]]
        picnic.append(can[i])
        bt(cann)
        picnic.pop()
    
k, n, f = map(int, input().split())
friend = [set() for _ in range(n+1)]
picnic = []

for _ in range(f):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)
    
can = [i for i in range(1, n+1) if len(friend[i]) >= k-1]
bt(can)

print(-1)