import sys
input = sys.stdin.readline

n = int(input())
k = n

for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        k *= (1 - 1/i)

if n > 1:
    k = k * (1-(1/n))

print(int(k))