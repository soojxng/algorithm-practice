import sys
input = sys.stdin.readline

preorder = []
inorder = []
postorder = []

def order(n):
    l, r = trees[n]
    preorder.append(n)
    if l != '.':
        order(l)
    inorder.append(n)
    if r != '.':
        order(r)
    postorder.append(n)

trees = dict()
for _ in range(int(input())):
    a, b, c = input().strip().split()
    trees[a] = [b, c]
order('A')
print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))