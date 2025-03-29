import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def euc(a, b):
    if b > a: a, b = b, a
    a = a % b
    if a == 0: return b
    else: return euc(b, a)
    
gcd = euc(n, m)
lcm = n * m // gcd

print(gcd)
print(lcm)