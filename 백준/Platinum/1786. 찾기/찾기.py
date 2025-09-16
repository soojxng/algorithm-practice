import sys
input = sys.stdin.readline

t = input().rstrip()
p = input().rstrip()

pi = [0]*len(p)
j = 0
for i in range(1, len(p)):
    while j > 0 and p[i] != p[j]:
        j = pi[j-1]
    if p[i] == p[j]:
        j += 1
        pi[i] = j

ans = []
j = 0
for i in range(len(t)):
    while j > 0 and t[i] != p[j]:
        j = pi[j-1]
    if t[i] == p[j]:
        if j == len(p)-1:
            ans.append(i-len(p)+2)
            j = pi[j]
        else:
            j += 1
print(len(ans))
print(*ans)