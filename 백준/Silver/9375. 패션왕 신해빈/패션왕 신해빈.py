import sys
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = dict()
    for __ in range(int(input())):
        tmp = input().strip().split()
        if tmp[1] not in clothes:
            clothes[tmp[1]] = 1
        clothes[tmp[1]] += 1
        
    ans = 1
    for n in clothes.values():
        ans *= n  
    print(ans - 1)