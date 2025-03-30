import sys
input = sys.stdin.readline

s = []

for _ in range(int(input())):
    tmp = input().split()
    if tmp[0] == 'push': s.append(tmp[1])
    elif tmp[0] == 'pop': print(s.pop() if s else -1)
    elif tmp[0] == 'size': print(len(s))
    elif tmp[0] == 'empty': print(0 if s else 1)
    elif tmp[0] == 'top': print(s[-1] if s else -1)