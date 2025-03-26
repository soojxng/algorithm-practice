import sys
input = sys.stdin.readline

n = int(input())
f = [0, 1, 1]
cnt_r = 0
cnt_dp = n - 2

def fib(n):
    global cnt_r
    if n == 1 or n == 2:
        cnt_r += 1
        return 1
    else: return (fib(n - 1) + fib(n - 2))

fib(n)

print(cnt_r, cnt_dp)