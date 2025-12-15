import sys
input = sys.stdin.readline

while 1:
    try:
        m, q = map(int, input().split())
        f = list(map(int, input().split()))
        g = list(map(int, input().split()))
        h = list(map(int, input().split()))

        for _ in range(q):
            a, b = map(int, input().split())
            y = a ^ g[h[a]^b]
            x = h[a] ^ b ^ f[y]
            print(x, y)
            
    except:
        break