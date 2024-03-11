def solution(want, number, discount):
    answer = 0
    dic = {}
    for i, v in enumerate(want):
        dic[v] = number[i]
    
    for i in range(len(discount)-9):
        tmp = discount[i: i+10]
        dic2 = {}
        for i in tmp:
            dic2[i] = dic2.get(i,0) + 1
        if dic == dic2:
            answer += 1
    return answer