import sys
input = sys.stdin.readline
from collections import deque 

n = int(input())
d = dict()
tree = [[] for _ in range(26)]
for _ in range(n):
    nickname = input().rstrip()
    if nickname in d:
        d[nickname] += 1
        print(f'{nickname}{d[nickname]}')
        continue
    else:
        d[nickname] = 1
    tmp = ord(nickname[0]) - ord('a')
    i = 0
    f = -1
    while i < len(nickname):
        for x, uid in tree[tmp]:
            if nickname[i] == x:
                tmp = uid
                break
        else:
            if f == -1:
                f = i+1
            tree[tmp].append((nickname[i], len(tree)))
            tree.append([])
            tmp = len(tree) - 1

        i += 1
    print(nickname[:f if f != -1 else i])