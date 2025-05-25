def cal(arr, b):
    if b <= 1:
        return [[x % (10**9+7) for x in a] for a in arr]
    tmp = cal(arr, b//2)
    ans = mul(tmp, tmp)
    if b % 2 == 1:
        ans = mul(ans, arr) 
    return ans

def mul(arr, arr2):
    N = len(arr)
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += arr[i][k] * arr2[k][j]
            tmp[i][j] %= (10**9+7)
    return tmp
    
n = int(input())
A = [[1, 1], [1, 0]]
C = cal(A, n-1)

print(C[0][0])