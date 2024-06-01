def solution(d, budget):
    while sum(d) > budget:
        d.remove(max(d))
    return len(d)