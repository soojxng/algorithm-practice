import sys
input = sys.stdin.readline

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        arr[pb] = pa
        ans[pa] += ans[pb]
    return ans[pa]

for _ in range(int(input())):
    dic = dict()
    arr = []
    ans = []
    for i in range(int(input())):
        a, b = input().rstrip().split()
        for x in (a, b):
            if x not in dic:
                dic[x] = len(arr)
                arr.append(dic[x])
                ans.append(1)
        print(union(dic[a], dic[b]))