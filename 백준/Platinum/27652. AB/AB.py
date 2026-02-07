import sys
input = sys.stdin.readline

q = int(input())
A = [[] for _ in range(27)]
B = [[] for _ in range(27)]
A[0] = [[i, chr(i + ord('a') - 1), 0] for i in range(1, 27)]
B[0] = [[i, chr(i + ord('a') - 1), 0] for i in range(1, 27)]

for _ in range(q):
    tmp = tuple(input().rstrip().split())
    if tmp[0] == 'add':
        s = tmp[2]
        x = 0
        if tmp[1] == 'A':
            for i in range(len(s)):
                f = 1
                for j in range(len(A[x])):
                    k, a, cnt = A[x][j]
                    if a == s[i]:
                        A[x][j][2] += 1
                        x = k
                        f = 0
                        break
                if f:
                    A[x].append([len(A), s[i], 1])
                    x = len(A)
                    A.append([])
        else:
            for i in range(len(s)-1, -1, -1):
                f = 1
                for j in range(len(B[x])):
                    k, b, cnt = B[x][j]
                    if b == s[i]:
                        B[x][j][2] += 1
                        x = k
                        f = 0
                        break
                if f:
                    B[x].append([len(B), s[i], 1])
                    x = len(B)
                    B.append([])
            
    elif tmp[0] == 'delete':
        s = tmp[2]
        x = 0
        if tmp[1] == 'A':
            for i in range(len(s)):
                f = 1
                for j in range(len(A[x])):
                    k, a, cnt = A[x][j]
                    if a == s[i]:
                        A[x][j][2] -= 1
                        x = k
                        f = 0
                        break
        else:
            for i in range(len(s)-1, -1, -1):
                f = 1
                for j in range(len(B[x])):
                    k, b, cnt = B[x][j]
                    if b == s[i]:
                        B[x][j][2] -= 1
                        x = k
                        f = 0
                        break

    elif tmp[0] == 'find':
        s = tmp[1]
        results = [0]*(len(s)-1)
        x = 0
        for i in range(len(s)-1):
            f = 1
            for j, a, cnt in A[x]:
                if a == s[i]:
                    results[i] = cnt
                    x = j
                    f = 0
                    break
            if f:
                break
        x = 0
        for i in range(len(s)-1, 0, -1):
            f = 1
            for j, b, cnt in B[x]:
                if b == s[i]:
                    results[i-1] *= cnt
                    x = j
                    f = 0
                    break
            if f:
                results = results[i:]
                break
        print(sum(results) if results else 0)