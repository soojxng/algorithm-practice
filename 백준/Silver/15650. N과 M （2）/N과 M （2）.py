import sys
input = sys.stdin.readline

def combination():
    if len(tmp) == M:
        print(" ".join(map(str, tmp)))
        return
    
    for i in range(1, N + 1):
        if i not in tmp:
            if not tmp or i + 1 > tmp[-1]:
                tmp.append(i)
                combination()
                tmp.pop()

N, M = map(int, input().split())
tmp = []            
combination()