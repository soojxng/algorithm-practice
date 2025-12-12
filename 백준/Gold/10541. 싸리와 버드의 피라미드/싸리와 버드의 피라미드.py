import sys
input = sys.stdin.readline

d = dict()
for i in range(ord('A'), ord('Z')+1):
    d[chr(i)] = i - ord('A')

n = int(input())
w = input().rstrip()
l = len(w)
psum = [[0]*26 for _ in range(l+1)]
for i in range(l):
    psum[i+1] = psum[i][::]
    psum[i+1][d[w[i]]] += 1

k = int(input())
for _ in range(k):
    a, c = input().rstrip().split()
    a = int(a)
    x = d[c]
    
    si = ((a-1)*a)//2
    ei = (a*(a+1))//2
    ans = (ei // l) * psum[l][x] + psum[ei % l][x]
    if si > 0:
        ans -= ((si // l) * psum[l][x] + psum[si % l][x])
    print(ans)