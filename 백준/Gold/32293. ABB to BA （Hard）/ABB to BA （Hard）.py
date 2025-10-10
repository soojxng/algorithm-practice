import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def add_b():
    if len(stack) >= 2 and stack[-2] == 'A' and stack[-1] == 'B':
        stack.pop()
        stack.pop()
        add_b()
        stack.append('A')
    else:
        stack.append('B')

t = int(input())
for _ in range(t):
    n = int(input())
    S = input().rstrip()
    stack = []
    for w in S:
        if w == 'A':
            stack.append('A')
        else:
            add_b()
    print(''.join(stack))