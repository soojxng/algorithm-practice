import sys
input = sys.stdin.readline
    
t = int(input())
for _ in range(t):
    a, b = input().rstrip().split()
    if len(a) != len(b):
        print(-1)
    else:
        ans = 0
        length = len(a)
        j = 0
        for i in range(length):
            if a[i] == 'a':
                while b[j] != 'a':
                    j += 1
                ans += abs(i-j)
                j += 1
        print(ans)