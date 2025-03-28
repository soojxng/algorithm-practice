import sys
input = sys.stdin.readline

L = int(input())
abc = input().strip()
r = 1
M = 1234567891

H = 0

for i in abc:
    H = (H + (ord(i) - ord('a') + 1) * r) % M
    r = (r*31) % M
    
print(H)