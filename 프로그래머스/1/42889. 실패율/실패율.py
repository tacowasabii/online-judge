def solution(N, stages):
    total = len(stages)
    dic = {}
    for i in sorted(list(set(stages))):
        if i <= N:
            dic[i] = stages.count(i) / total
            total -= stages.count(i)
    for i in range(1, N+1):
        dic[i] = dic.get(i,0)
    return sorted(dic, key=lambda x: dic[x], reverse=True) 