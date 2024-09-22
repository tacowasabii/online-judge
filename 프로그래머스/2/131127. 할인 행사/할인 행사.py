from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for i, v in enumerate(want):
        dic[v] = number[i]
    
    for i in range(len(discount) - sum(number) + 1):
        discount_dict = Counter(discount[i:i + sum(number)])
        flag = True
        for j in want:
            if dic[j] != discount_dict[j]:
                flag = False
        if flag:
            answer += 1
    return answer