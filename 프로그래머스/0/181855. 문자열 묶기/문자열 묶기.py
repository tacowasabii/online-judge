def solution(strArr):
    answer = 0
    dic = {}
    for i in strArr:
        dic[len(i)] = dic.get(len(i),0) + 1
    for i,v in dic.items():
        answer = max(answer,v)
    return answer