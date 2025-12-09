import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, s = input().rstrip().split()
    n = int(n)
    s = list(s)
    s.append('')

    shortest = []
    longest = []
    ss = []
    ls = []
    for i in range(n):
        ss.append(n-i)
        ls.append(i+1)
        if s[i] == '<':
            while ls:
                longest.append(ls.pop())
        elif s[i] == '>':
            while ss:
                shortest.append(ss.pop())
        else:
            shortest += ss[::-1]
            longest += ls[::-1]

    print(*shortest)
    print(*longest)