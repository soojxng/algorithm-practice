import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, cnt):
    if len(tree[i]) == 0:
        return
    tree[i].sort()
    for dir, j in tree[i]:
        tmp = ' '*cnt + dir
        print(tmp)
        dfs(j, cnt+1)


root = dict()
tree = []

n = int(input())
for _ in range(n):
    tmp = input().rstrip().split('\\')
    if tmp[0] in root:
        x = root[tmp[0]]
    else:
        x = len(tree)
        root[tmp[0]] = x
        tree.append([])
    for i in range(1, len(tmp)):
        f = 1
        for dir, j in tree[x]:
            if dir == tmp[i]:
                x = j
                f = 0
                break
        if f:
            tree[x].append((tmp[i], len(tree)))
            x = len(tree)
            tree.append([])

for dir in sorted(root.keys()):
    print(dir)
    dfs(root[dir], 1)