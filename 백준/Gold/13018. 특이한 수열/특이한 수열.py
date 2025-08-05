n, k = map(int, input().split())
if n == k:
    print('Impossible')
else:
    for i in range(2, n-k+1):
        print(i, end=' ')
    print(1, end=' ')
    for i in range(n-k+1, n+1):
        print(i, end=' ')