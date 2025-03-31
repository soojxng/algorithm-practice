import sys
input = sys.stdin.readline

q = []
f = -1
r = -1

for _ in range(int(input())):
    tmp = input().split()
    if tmp[0] == 'push': q.append(tmp[1]); r += 1
    elif tmp[0] == 'pop':
        if f != r:
            f += 1
            print(q[f])
        else:
            print(-1)
    elif tmp[0] == 'size': print(r - f)
    elif tmp[0] == 'empty': print(1 if f == r else 0)
    elif tmp[0] == 'front': print(q[f + 1] if f != r else -1)
    elif tmp[0] == 'back': print(q[r] if f != r else -1)