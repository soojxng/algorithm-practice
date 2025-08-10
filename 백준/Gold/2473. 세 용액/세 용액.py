import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
ans = [float('inf')]

for k in range(0, N-2):
    if ans[0] == 0:
        break
    i = k+1
    j = N-1
    while i < j:
        tmp = A[i] + A[j] + A[k]
        ans = min(ans, [abs(tmp), A[k], A[i], A[j]])
        if tmp == 0:
            break
        elif tmp < 0:
            i += 1
        else:
            j -= 1
print(ans[1], ans[2], ans[3])