N = int(input())
P = sorted(map(int, input().split()), reverse=1)

print(sum((i+1)*p for i, p in enumerate(P)))