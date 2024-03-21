def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        dic[i] = dic.get(i,0) + 1
    sort = sorted(dic.items(), key = lambda x:x[1], reverse = True)\
    
    cnt = 0
    for i,v in enumerate(sort):
        cnt += v[1]
        if cnt >= k:
            return i+1