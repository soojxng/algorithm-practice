import sys
input = sys.stdin.readline

def dfs(v):
    if len(tree[v]) == 0:
        m[v] = ' '
        return 0 if sizes[v] < t else 1
    
    f = 0
    for u in tree[v].values():
        f |= dfs(u)
    m[v] = '-' if f else '+'

    return 0 if sizes[v] < t else 1

def printResult(v, path):
    p = ('/' + '/'.join(path) + '/') if v != 0 else '/'
    print(f'{m[v]} {p} {sizes[v]}')
    if m[v] == '-':
        for d in sorted(tree[v].keys()):
            path.append(d)
            printResult(tree[v][d], path)
            path.pop()

n = int(input())
tree = [dict()]
sizes = [0]

for _ in range(n):
    tmp = input().rstrip().split()
    path = tmp[0].split('/')
    size = int(tmp[1])
    u = 0
    sizes[0] += size
    for i in range(1, len(path)-1):
        nu = -1
        if path[i] in tree[u]:
            nu = tree[u][path[i]]
        else:
            nu = len(tree)
            tree[u][path[i]] = nu
            tree.append(dict())
            sizes.append(0)
        sizes[nu] += size
        u = nu

t = int(input())

m = [0]*len(tree)
_ = dfs(0)
printResult(0, [])