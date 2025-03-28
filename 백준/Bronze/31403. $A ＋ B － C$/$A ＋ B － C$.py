import sys
input = sys.stdin.readline

l = []

for _ in range(3):
    l.append(int(input()))
    
print(l[0] + l[1] - l[2])
print(int(str(l[0]) + str(l[1])) - l[2])