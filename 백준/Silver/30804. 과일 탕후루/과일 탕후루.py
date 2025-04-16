N = int(input())
tangs = list(map(int, input().split()))
fruits = [[0, 0]]

for t in tangs:
    if fruits[-1][0] == t:
        fruits[-1][1] += 1
    else:
        fruits.append([t, 1])
       
s = set()
ans = 0
cnt = 0
for i in range(1, len(fruits)):
    if fruits[i][0] not in s and len(s) == 2:
        ans = max(ans, cnt)
        s = {fruits[i-1][0], fruits[i][0]}
        cnt = fruits[i-1][1] + fruits[i][1]
    else:
        s.add(fruits[i][0])
        cnt += fruits[i][1]
        
print(max(ans, cnt))