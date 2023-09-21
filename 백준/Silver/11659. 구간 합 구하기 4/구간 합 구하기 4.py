import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0 for _ in range(n + 1)]

for i in range(n):
    sum_arr[i+1] = sum_arr[i] + arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(sum_arr[b] - sum_arr[a-1])