n = int(input())
num_list = map(int, input().split())
m = int(input())
find_list = map(int, input().split())
dic = dict()

for num in num_list:
    if num in dic:
        dic[num] = dic[num] + 1
    else:
        dic[num] = 1
for num in find_list:
    if num in dic:
        print(dic[num], end=' ')
    else:
        print("0", end=' ')