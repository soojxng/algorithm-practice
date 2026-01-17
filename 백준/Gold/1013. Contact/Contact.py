import sys
import re
input = sys.stdin.readline

p = re.compile(r'(100+1+|01)+$')

for _ in range(int(input())):
    s = input().rstrip()
    print('YES' if p.match(s) else 'NO')