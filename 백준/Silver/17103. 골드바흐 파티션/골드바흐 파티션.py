import sys

t = int(input())

arr = [True for _ in range(1000001)]
for i in range(2,1001):
    if arr[i]:
        for j in range(i + i , 1000001, i):
            arr[j] = False

for _ in range(t):
    result = 0
    n = int(sys.stdin.readline().rstrip())

    for i in range(2,n//2+1):
        if arr[i] and arr[n-i]:
            result += 1
    print(result)