import sys
from collections import deque
input = sys.stdin.readline
    
def cal(a, b, o):
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '*':
        return a*b
    else:   #elif o == '/':
        return (abs(a) // abs(b)) if (a < 0) == (b < 0) else -(abs(a) // abs(b))
    
def calLeft():
    a = nums.popleft()
    b = nums.popleft()
    nums.appendleft(cal(a, b, ops.popleft()))

def calRight():
    b = nums.pop()
    a = nums.pop()
    nums.append(cal(a, b, ops.pop()))
    
e = input().rstrip()
nums = deque()
ops = deque()
i = 0
tmp = 0
if e[0] == '-':
    i = 1
    while i < len(e) and e[i].isdigit():
        tmp = (tmp*10) + int(e[i])
        i += 1
    tmp = -tmp

for j in range(i, len(e)):
    x = e[j]
    if x.isdigit():
        tmp = (tmp*10) + int(x)
    else:
        nums.append(tmp)
        ops.append(x)
        tmp = 0
nums.append(tmp)

prio = {'+': 0, '-': 0, '*': 1, '/': 1}
while ops:
    if prio[ops[0]] > prio[ops[-1]]:
        calLeft()
    elif prio[ops[0]] < prio[ops[-1]]:
        calRight()
    else:
        l = cal(nums[0], nums[1], ops[0])
        r = cal(nums[-2], nums[-1], ops[-1])
        if l >= r:
            calLeft()
        else:
            calRight()

print(nums.pop())