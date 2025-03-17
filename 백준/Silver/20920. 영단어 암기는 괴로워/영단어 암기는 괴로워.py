import sys
from collections import Counter
input = sys.stdin.readline

N = list(map(int, input().split()))
words = []

for _ in range(N[0]):
    tmp = input().rstrip()
    if len(tmp) >= N[1]:
        words.append(tmp)
        
freq = Counter(words)

result = sorted(freq.keys(), key = lambda x : (-freq[x], -len(x), x))

for w in result:
    print(w)