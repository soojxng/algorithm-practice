import sys
input = sys.stdin.readline

def bt(i, s, vo):    
    if len(s) == l:
        if vo > 0 and l-vo > 1:
            print(''.join(s))
        return
    if i >= c:
        return
    
    s.append(a[i])
    bt(i+1, s, vo + (1 if a[i] in vow else 0))
    s.pop()
    bt(i+1, s, vo)

l, c = map(int, input().split())
a = list(input().rstrip().split())
vow = {'a', 'e', 'i', 'o', 'u'}

a.sort()
bt(0, [], 0)