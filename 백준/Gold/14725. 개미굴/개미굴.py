import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, cnt):
    if len(tree[i]) == 0:
        return
    tree[i].sort()
    for food, j in tree[i]:
        tmp = '--'*cnt + food
        print(tmp)
        dfs(j, cnt+1)


root = dict()
tree = []

n = int(input())
for _ in range(n):
    tmp = input().rstrip().split()
    if tmp[1] in root:
        x = root[tmp[1]]
    else:
        x = len(tree)
        root[tmp[1]] = x
        tree.append([])
    for i in range(2, int(tmp[0])+1):
        f = 1
        for food, j in tree[x]:
            if food == tmp[i]:
                x = j
                f = 0
                break
        if f:
            tree[x].append((tmp[i], len(tree)))
            x = len(tree)
            tree.append([])

for food in sorted(root.keys()):
    print(food)
    dfs(root[food], 1)