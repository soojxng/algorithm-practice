import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input().rstrip()
    k = int(input())
    arr = [[] for _ in range(26)]
    min_val = float('inf')
    max_val = -1

    for i in range(len(w)):
        x = ord(w[i]) - ord('a')
        arr[x].append(i)
        
    for i in range(26):
        for j in range(k-1, len(arr[i])):
            tmp = arr[i][j] - arr[i][j-k+1] + 1
            min_val = min(min_val, tmp)
            max_val = max(max_val, tmp)

    if max_val != -1:
        print(min_val, max_val)
    else:
        print(-1)