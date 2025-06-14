N = int(input())
A = sorted(list(map(int, input().split())))
i = 0
j = N-1
ans = [float('inf')]
while i < j:
    tmp = A[i] + A[j]
    ans = min(ans, [abs(tmp), A[i], A[j]])
    if tmp == 0:
        break
    elif tmp < 0:
        i += 1
    else:
        j -= 1
print(ans[1], ans[2])