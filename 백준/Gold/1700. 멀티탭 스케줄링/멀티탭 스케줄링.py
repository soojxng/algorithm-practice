import sys
input = sys.stdin.readline

n, k = map(int, input().split())
order = list(map(int, input().split()))
li = [[] for _ in range(k+1)]
for i in range(k-1, -1, -1):
    li[order[i]].append(i)

s = set()
ans = 0
for i in range(k):
    li[order[i]].pop()
    if order[i] in s:
        continue
    elif len(s) < n:
        s.add(order[i])
    else:
        max_val = -1
        max_ind = -1
        for j in s:
            if not li[j]:
                max_ind = j
                break
            elif max_val < li[j][-1]:
                max_val = li[j][-1]
                max_ind = j
        s.remove(max_ind)
        ans += 1
        s.add(order[i])
print(ans)