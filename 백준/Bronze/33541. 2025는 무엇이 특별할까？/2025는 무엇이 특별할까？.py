import sys
input = sys.stdin.readline

year = []
for i in range(32, 100):
    x2 = i * i
    y = x2 // 100 + x2 % 100
    if i == y:
        year.append(x2)
        
X = int(input())
Y = -1
for y in year:
    if y > X:
        Y = y
        break
print(Y)