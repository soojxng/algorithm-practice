import sys
input = sys.stdin.readline

N = int(input())

S = set(['ChongChong'])

for _ in range(N):
    tmp = set(input().strip().split(' '))
    if tmp & S:
        S = S.union(tmp)
        
print(len(S))