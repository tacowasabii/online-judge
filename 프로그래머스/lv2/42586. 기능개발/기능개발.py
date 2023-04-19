from math import ceil

def solution(progresses, speeds):
    days = []
    ans = []
    for i in range(len(progresses)):
        days.append(ceil((100.0 - progresses[i]) / speeds[i]))
    tmp = days[0]
    cnt = 0
    for i in days:
        if tmp >= i:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            tmp = i
    ans.append(cnt)
    return ans