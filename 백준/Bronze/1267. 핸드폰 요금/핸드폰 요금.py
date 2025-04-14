N = int(input())
calls = list(map(int, input().split()))

y = sum((t // 30 + 1)*10 for t in calls)
m = sum((t // 60 + 1)*15 for t in calls)

print(f'Y {y}' if y < m else (f'Y M {y}' if y == m else f'M {m}'))