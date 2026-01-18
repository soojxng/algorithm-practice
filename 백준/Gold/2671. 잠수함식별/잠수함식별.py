import sys
import re
input = sys.stdin.readline

p = re.compile(r'(100+1+|01)+$')

s = input().rstrip()
print('SUBMARINE' if p.match(s) else 'NOISE')