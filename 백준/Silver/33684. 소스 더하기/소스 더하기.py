N, K = map(int, input().split())
sauces = sorted(list(map(int, input().split())), reverse=1)
minimum = sauces[-1]

if sauces[0] > K:
    print(0)
elif minimum <= 0:
    print(-1)
else:
    minimum = sauces[-1]
    sauces.pop()
    cnt = [(K - s) // minimum for s in sauces]
    print(sum(cnt)+1)