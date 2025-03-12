import sys
from collections import deque

class Deque:
    def __init__(self):
        self.d = deque()
        self.func_arr = [self.appendFront, self.appendRear, self.popFront, self.popRear, self.printLen, self.printIsEmpty, self.printFront, self.printRear]

    def appendFront(self, x):
        self.d.appendleft(x)

    def appendRear(self, x):
        self.d.append(x)

    def popFront(self):
        print(self.d.popleft() if self.d else -1)

    def popRear(self):
        print(self.d.pop() if self.d else -1)

    def printLen(self):
        print(len(self.d))
        
    def printIsEmpty(self):
        print(int(not self.d))
        
    def printFront(self):
        print(self.d[0] if self.d else -1)
    
    def printRear(self):
        print(self.d[-1] if self.d else -1)

    def func(self, n, *x):
        self.func_arr[n-1](*x)
    
        
N = int(sys.stdin.readline())
deq = Deque()

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    deq.func(tmp[0], *tmp[1:])