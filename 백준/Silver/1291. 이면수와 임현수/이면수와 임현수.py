def check_odd(n):
    cnt = 0
    while n > 0:
        cnt += n % 10
        n //= 10
    return cnt % 2

def check_prime_factors(n):
    s = set()
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            s.add(i)
        else:
            i += 1
    if n > 1: s.add(n)
    return len(s) % 2 == 0

def is_ems(n):
    if n > 6 and check_odd(n):
        return 1
    else: return 0
    
def is_ihs(n):
    if n == 2 or n == 4:
        return 1
    elif n != 1 and check_prime_factors(n):
        return 1
    else: return 0

N = int(input())
ems = is_ems(N)
ihs = is_ihs(N)

if ems and ihs:
    print(4)
elif ems:
    print(1)
elif ihs:
    print(2)
else:
    print(3)
