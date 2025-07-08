import sys
input = sys.stdin.readline

for _ in range(int(input())):
    P, Q, A, B, C, D = map(int, input().split())
    R = (Q//C) * D
    P += (R//B) * A
    R %= B
    
    x = (P-R)//(A+B)
    ans = max(min(R + (B*x), P-(A*x)), min(R+(B*(x+1)), P-(A*(x+1))))
    print(ans)