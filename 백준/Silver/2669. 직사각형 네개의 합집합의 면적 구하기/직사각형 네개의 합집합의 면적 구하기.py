r = [[0 for _ in range(101)] for __ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2)):
        for j in range(min(y1, y2), max(y1, y2)):
            r[i][j] = 1
            
print(sum(sum(rr) for rr in r))