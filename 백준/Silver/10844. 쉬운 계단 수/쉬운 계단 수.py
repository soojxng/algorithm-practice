N = int(input())
arr = [1 for _ in range(10)]
arr[0] = 0

for _ in range(1, N):
    tmp = [0 for _ in range(10)]
    for i in range(10):
        a = 0 if i-1 < 0 else arr[i-1]
        b = 0 if i+1 > 9 else arr[i+1]
        tmp[i] = (a + b) % 1000000000
    arr = tmp
    
print(sum(arr) % 1000000000)