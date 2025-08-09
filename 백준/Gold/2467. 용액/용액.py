import sys
input = sys.stdin.readline
        
n = int(input())
sol = list(map(int, input().split()))

i = 0
j = n-1
x = float('inf')
ans = [0, 0]

while i < j:
    tmp = sol[i] + sol[j]
    if abs(tmp) < x:
        x = abs(tmp)
        ans = [sol[i], sol[j]]
        
    if tmp == 0:
        break
    elif tmp > 0:
        j -= 1
    else:
        i += 1
        
print(*ans)