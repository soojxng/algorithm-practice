def find(a, b):
    if a%b == 0:
        return int(b)
    else:
        return find(b, (a%b))

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    ans = a * b // find(a, b)
    print(ans)