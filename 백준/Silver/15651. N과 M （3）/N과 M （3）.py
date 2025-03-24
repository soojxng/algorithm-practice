import sys
input = sys.stdin.readline

def permutation_rep():
    if len(tmp) == M:
        print(" ".join(map(str, tmp)))
        return
    
    for i in range(1, N + 1):
        tmp.append(i)
        permutation_rep()
        tmp.pop()

N, M = map(int, input().split())
tmp = []            
permutation_rep()