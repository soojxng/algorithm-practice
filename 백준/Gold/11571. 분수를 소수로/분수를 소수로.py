import sys
input = sys.stdin.readline

for t in range(int(input())):
    a, b = map(int, input().split())
    print(f'{a//b}.', end='')
    a = (a % b) * 10
    d = dict()
    ans = []
    while 1:
        if a in d:
            print(f"{''.join(ans[:d[a]])}({''.join(ans[d[a]:])})")
            break
        d[a] = len(ans)
        ans.append(str(a//b))
        a = (a % b) * 10
