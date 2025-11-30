import sys
input = sys.stdin.readline

a = input().rstrip()
size = len(a)
d = dict()
for i in range(ord('a'), ord('z')+1):
    d[chr(i)] = 0
for i in range(size):
    d[a[i]] |= (1 << i)

q = int(input())
for _ in range(q):
    tmp = input().rstrip()
    s = tmp[0]
    n = int(tmp[1:-1])
    e = tmp[-1]
    result = (d[s] & ((1 << (size - n - 1))-1)) & (d[e] >> (n+1))
    print(result.bit_count())