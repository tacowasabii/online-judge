from math import ceil

def solution(progresses, speeds):
    tmp = []
    ans = []
    
    for i, v in enumerate(progresses):
        tmp.append(ceil((100-v)/speeds[i]))
    
    cnt = 0
    start = tmp[0]
    for i, v in enumerate(tmp):
        cnt += 1
        if i != len(tmp) - 1:
            if start < tmp[i + 1]:
                ans.append(cnt)
                cnt = 0
                start = tmp[i + 1]
        else:
             ans.append(cnt)
    return ans