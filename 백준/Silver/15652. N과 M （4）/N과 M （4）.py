import sys
input = sys.stdin.readline

def combination_rep(start):
    if len(tmp) == M:
        print(" ".join(map(str, tmp)))
        return
    
    for i in range(start, N + 1):
        tmp.append(i)
        combination_rep(i)
        tmp.pop()

N, M = map(int, input().split())
tmp = []            
combination_rep(1)