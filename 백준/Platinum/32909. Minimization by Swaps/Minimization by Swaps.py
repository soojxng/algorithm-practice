import sys
from collections import deque
input = sys.stdin.readline

def add(i, v):
    while i <= len(s):
        fw[i] += v
        i += i & -i

def sum(i):
    x = 0
    while i > 0:
        x += fw[i]
        i -= i & -i
    return x

t = int(input())
for _ in range(t):
    s, k = input().rstrip().split()
    s = list(s)
    k = int(k)
    
    nums = [deque([]) for _ in range(10)]
    fw = [0] * (len(s) + 1)
    for i in range(len(s)):
        nums[int(s[i])].append(i)
        add(i+1, 1)

    ans = []
    i = 0
    while i < len(s) and k > 0:
        f = 0

        for n in range(1, 10):
            if not nums[n]:
                continue

            tmp = sum(nums[n][0]+1) - 1
            if tmp <= k:
                k -= tmp
                ans.append(n)
                add(nums[n][0]+1, -1)
                nums[n].popleft()
                i += 1
                f = 1
                break

        if not f:
            break

    tmp = []
    for n in range(1, 10):
        for i in nums[n]:
            tmp.append((i, n))
    tmp.sort()
    for i, n in tmp:
        ans.append(n)

    print(''.join(map(str, ans)))