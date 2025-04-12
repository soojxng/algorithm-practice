import sys
input = sys.stdin.readline

for _ in range(3):
    total = 0
    for __ in range(int(input())):
        total += int(input())
    print('+' if total > 0 else ('-' if total < 0 else '0'))