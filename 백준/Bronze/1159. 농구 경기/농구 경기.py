import sys
input = sys.stdin.readline

names = dict()

for _ in range(int(input())):
    tmp = input().strip()[0]
    if tmp in names:
        names[tmp] += 1
    else:
        names[tmp] = 1

s = ''

for name in sorted(names):
    if names[name] >= 5:
        s += name

print(s if s else 'PREDAJA')