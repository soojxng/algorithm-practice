import sys
input = sys.stdin.readline

N = int(input())

S = set()
cnt = 0

for _ in range(N):
    tmp = input().strip()
    if tmp == 'ENTER':
        cnt += len(S)
        S = set()
    else:
        S.add(tmp)
        
print(cnt + len(S))