import sys
input = sys.stdin.readline

def insert(x):
    i = len(heap)
    heap.append((abs(x), x))
    while i // 2 != 0 and heap[i//2] > heap[i]:
        heap[i//2], heap[i] = heap[i], heap[i//2]
        i = i//2
    
def pop():
    if len(heap) == 1:
        print(0)
    elif len(heap) == 2:
        print(heap.pop()[1])
    else:
        print(heap[1][1])
        heap[1] = heap.pop()
        
        i = 1
        while 1:
            p = (heap[i], i)
            c1 = (heap[i*2] if i*2 < len(heap) else (float('inf'), float('inf')), i*2)
            c2 = (heap[i*2+1] if i*2+1 < len(heap) else (float('inf'), float('inf')), i*2+1)
            
            m = min(p, c1, c2)[1]
            if m == i:
                break
            heap[i], heap[m] = heap[m], heap[i]
            i = m

heap = [0]

for _ in range(int(input())):
    tmp = int(input())
    if tmp == 0: pop()
    else: insert(tmp)