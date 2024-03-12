def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        dic[i[1]] = dic.get(i[1],0) + 1
    for v in dic.values():
        answer *= v + 1
    return answer - 1