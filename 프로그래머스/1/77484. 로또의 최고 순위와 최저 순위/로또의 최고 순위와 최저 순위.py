def getRank(n):
    if n == 0 or n == 1:
        return 6
    else:
        return 7 - n

def solution(lottos, win_nums):
    zero = 0
    same = 0
    for i in lottos:
        if i in win_nums:
            same += 1
        elif i == 0:
            zero += 1
    return [getRank(same + zero), getRank(same)]