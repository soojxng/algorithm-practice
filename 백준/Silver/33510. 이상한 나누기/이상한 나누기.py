N = int(input())
X = input().rstrip()[::-1]
cnt = 0
for i in range(X.find('1'), N-1):
    if cnt and X[i] == '0':
        cnt += 1
    elif cnt == 0 and X[i] == '1':
        cnt = 1
print(cnt)