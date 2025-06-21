A, B, N = map(int, input().split())
sosus = [1]*100
s = set([1, 3, 7, 9])
ans = ['1']*N
for i in range(2, 100):
    for j in range(i*i, 100, i):
        sosus[j] = 0
        
if not sosus[A] or not sosus[B]:
    print(-1)
elif B//10 not in s:
    print(-1)
else:
    ans[0] = str(A//10)
    ans[1] = str(A%10)
    if ans[1] == '9':
        ans[2] = '7'
    ans[-2] = str(B//10)
    ans[-1] = str(B%10)
    print(*ans, sep='')