import sys
input = sys.stdin.readline

name = dict()
task = dict()
arr = [[0]*10 for _ in range(10000)]

for _ in range(int(input())):
    n, t, s = input().rstrip().split()
    if n not in name:
        name[n] = len(name)
    if t not in task:
        task[t] = len(task)
    arr[name[n]][task[t]] = max(int(s), arr[name[n]][task[t]])
    
ans = [(sum(arr[name[n]]), n) for n in name.keys()]
ans.sort(reverse=1)
for s, n in ans:
    print(n, s)