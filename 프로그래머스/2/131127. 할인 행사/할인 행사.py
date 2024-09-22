from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for i, v in enumerate(want):
        dic[v] = number[i]
    
    for i in range(len(discount) - sum(number) + 1):
        if dic == Counter(discount[i:i + sum(number)]):
            answer += 1

    return answer