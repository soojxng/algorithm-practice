n = int(input())
x = sorted(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt += i*x[i] - (n-i-1)*x[i]
print(cnt*2)