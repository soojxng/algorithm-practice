import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=1)
boxes.sort(reverse=1)

ans = 0
if boxes[0] > cranes[0]:
    ans = -1
else:
    while boxes:
        for i in range(len(cranes)):
            if not boxes:
                break
            elif cranes[i] < boxes[-1]:
                break
            else:
                for j in range(len(boxes)):
                    if cranes[i] >= boxes[j]:
                        boxes.pop(j)
                        break
        ans += 1

print(ans)