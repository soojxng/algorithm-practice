import sys
input = sys.stdin.readline

def combination(start):
    if len(tmp) == M:
        print(" ".join(map(str, tmp)))
        return
    
    for i in range(start, N + 1):
        tmp.append(i)
        combination(i + 1)
        tmp.pop()

N, M = map(int, input().split())
tmp = []            
combination(1)
