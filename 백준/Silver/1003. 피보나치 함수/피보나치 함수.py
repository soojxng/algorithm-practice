import sys
input = sys.stdin.readline

fibo = [1, 0]
for _ in range(40):
    fibo.append(fibo[-2] + fibo[-1])

for _ in range(int(input())):
    n = int(input())
    print(fibo[n], fibo[n+1])