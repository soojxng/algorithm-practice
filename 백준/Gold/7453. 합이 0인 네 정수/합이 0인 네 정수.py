import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(4)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    arr[3].append(d)
    
ab = []
cd = []

for i in range(n):
    for j in range(n):
        ab.append(arr[0][i] + arr[1][j])
        cd.append(arr[2][i] + arr[3][j])
ab.sort()
cd.sort()

i = 0
j = n*n-1
cnt = 0

while i < len(ab) and j >= 0:
    if ab[i] + cd[j] == 0:
        ni = i+1
        nj = j-1
        while ni < len(ab) and ab[i] == ab[ni]:
            ni += 1
        while nj >= 0 and cd[j] == cd[nj]:
            nj -= 1
        cnt += (ni-i) * (j-nj)
        i = ni
        j = nj
    elif ab[i] + cd[j] < 0:
        i += 1
    else:
        j -= 1
        
print(cnt)