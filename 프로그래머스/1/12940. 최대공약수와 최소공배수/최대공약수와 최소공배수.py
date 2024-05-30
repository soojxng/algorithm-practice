def gcd(n, m):
    while n > 0:
        n, m = m % n, n
    return m

def solution(n, m):
    if n > m:
        n, m = m, n
    return [gcd(n, m), n*m//gcd(n, m)]