import sys
input = sys.stdin.readline

P = [0, 1, 1, 1] + [0] * 97

for i in range(4, 101):
    P[i] = P[i-3] + P[i-2]
    
for _ in range(int(input())):
    print(P[int(input())])