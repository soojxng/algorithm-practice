n = int(input())
A = sorted(list(map(int, input().split())))
x = int(input())
i = 0
j = n-1
cnt = 0
while i < j:
    tmp = A[i] + A[j]
    if tmp == x:
        cnt += 1
        i += 1
        j -= 1
    elif tmp < x:
        i += 1
    else:
        j -= 1
print(cnt)