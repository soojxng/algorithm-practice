def solution(lottos, win_nums):
    answer = [1 if i in win_nums else 0 for i in lottos]
    rank = [6, 6, 5, 4, 3, 2, 1]
    return [rank[sum(answer) + lottos.count(0)], rank[sum(answer)]]