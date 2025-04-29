import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
ans = set()

for i in range(1, N+1):
    if i not in ans and nums[i-1] not in ans:
        tmp = i
        s1 = set()
        s2 = set()
        while 1:
            if tmp in s1:
                break
            s1.add(tmp)
            tmp = nums[tmp-1]
            s2.add(tmp)
        if s1 == s2:
            ans = ans | s1
            
print(len(ans))
for n in sorted(ans):
    print(n)