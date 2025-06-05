import sys
input = sys.stdin.readline

N, K = map(int, input().split())
obs = set()
x, y = 0, 0
for _ in range(N):
    obs.add(tuple(map(int, input().split())))
for c in input().strip():
    if c == 'L' and x > -500 and (x-1, y) not in obs:
        x -= 1
    elif c == 'R' and x < 500 and (x+1, y) not in obs:
        x += 1
    elif c == 'U' and y < 500 and (x, y+1) not in obs:
        y += 1
    elif c == 'D' and y > -500 and (x, y-1) not in obs:
        y -= 1
print(x, y)