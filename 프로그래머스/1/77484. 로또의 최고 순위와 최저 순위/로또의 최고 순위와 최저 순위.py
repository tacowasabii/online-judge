def getRank(n):
    if n == 0 or n == 1:
        return 6
    else:
        return 7 - n

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    min = getRank(cnt)
    max = getRank(cnt + lottos.count(0))
        
    return [max,min]