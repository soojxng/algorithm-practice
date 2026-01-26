import sys
input = sys.stdin.readline  

s = input().rstrip()
if s[:len(s)//2] != s[::-1][:len(s)//2]:
    print(len(s))
else:
    if len(set(list(s))) == 1:
        print(-1)
    else:
        print(len(s)-1)