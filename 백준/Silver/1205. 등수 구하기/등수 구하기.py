N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    scores.append(new_score)
    scores.sort(reverse=1)
    i = scores.index(new_score)
    if i + scores.count(new_score) <= P:
        print(i+1)
    else:
        print(-1)