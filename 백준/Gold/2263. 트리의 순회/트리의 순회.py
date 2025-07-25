import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_pre(i, j, k, l):
    if i > j:
        return
    
    x = in_index[POST[l]]
    
    print(POST[l], end=' ')
    find_pre(i, x-1, k, k+x-i-1)
    find_pre(x+1, j, k+x-i, l-1)

n = int(input())
IN = list(map(int, input().split()))
POST = list(map(int, input().split()))
in_index = dict()
for i in range(n):
    in_index[IN[i]] = i
    
find_pre(0, n-1, 0, n-1)