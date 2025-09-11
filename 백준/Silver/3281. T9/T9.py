import sys
input = sys.stdin.readline

numd = dict()
x = 2
for i in range(65, 91):
    if i in (68, 71, 74, 77, 80, 84, 87):
        x += 1
    numd[chr(i)] = str(x)

wordd = dict()
for _ in range(int(input())):
    s = input().rstrip()
    tmp = [numd[c] for c in s]
    tmp = ''.join(tmp)
    if tmp not in wordd:
        wordd[tmp] = s

n = int(input())
s = input().rstrip().replace(' ', '').split('1')
ans = [wordd[w] if w in wordd else '*'*len(w) for w in s]

print(*ans)