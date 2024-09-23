from math import ceil

def solution(progresses, speeds):
    ans = []
    days = []
    for i, v in enumerate(progresses):
        days.append(ceil((100 - v) / speeds[i]))
    day = 0
    num = 0
    for i in days:
        if i > day:
            day = i
            ans.append(num)
            num = 1
        else:
            num += 1
    
    ans.append(num)
    return ans[1:]