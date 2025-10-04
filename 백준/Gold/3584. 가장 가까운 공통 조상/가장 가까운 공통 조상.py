import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    tree = [i for i in range(n+1)]
    root = -1
    for i in range(n-1):
        a, b = map(int, input().split())
        if root == b or root == -1:
            root = a
        tree[b] = a
    a, b = map(int, input().split())
    tmp = a
    parents = {root, a}
    while tmp != root:
        parents.add(tree[tmp])
        tmp = tree[tmp]
    if b in parents:
        print(b)
    else:
        tmp = b
        while 1:
            if tree[tmp] in parents:
                print(tree[tmp])
                break
            tmp = tree[tmp]