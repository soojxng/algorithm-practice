A, B, C = map(int, input().split())

def AB(A, B):
    if B == 0:
        return 1
    tmp = AB(A, B//2)
    if B % 2 == 1:
        return (tmp * tmp * A) % C
    else:
        return (tmp * tmp) % C
    
print(AB(A, B))