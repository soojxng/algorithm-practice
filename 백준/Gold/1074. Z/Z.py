N, r, c = map(int, input().split())
x1, x2, y1= 0, 2**N, 0
cnt = 0
while x2 - x1 > 1:
    d = (x2-x1)//2
    dx = x1+d
    dy = y1+d
    if r < dx and c < dy:
        x2 = dx
    elif dx <= r and c < dy:
        cnt += 2*(d**2)
        x1 = dx
    elif r < dx and dy <= c:
        cnt += (d**2)
        x2 = dx
        y1 = dy
    elif dx <= r and dy <= c:
        cnt += 3*(d**2)
        x1 = dx
        y1 = dy
        
print(cnt)