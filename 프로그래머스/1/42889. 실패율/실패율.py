def solution(N, stages):
    dic = {}
    for i in range(1, N + 1):
        dic[i] = 0
    for i in stages:
        if i in dic:
            dic[i] += 1
    total = len(stages)
    
    fail = {}
    for i in range(1, N + 1):
        if total != 0:
            fail[i] = dic[i] / total
        else:
            fail[i] = 0
        total -= dic[i]
    
    return sorted(fail, reverse = True, key = lambda x:fail[x])