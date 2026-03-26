import sys
input = sys.stdin.readline
    
n = int(input())
q = list(map(float, input().split()))
r = list(map(float, input().split()))
pref = [0]*n
pref[-1] = r[-1]
for i in range(n-2, -1, -1):
    pref[i] = pref[i+1] + r[i]

p = [q[i] / pref[i] for i in range(n)]
psum = sum(p)
p = [p[i] / psum for i in range(n)]
print(*p)