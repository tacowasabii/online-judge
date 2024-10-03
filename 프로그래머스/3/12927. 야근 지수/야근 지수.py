from collections import Counter

def solution(n, works):
    result = 0
    max_ = max(works)
    dic = Counter(works)
    
    while n > 0:
        if dic[max_] >= n:
            dic[max_] -= n
            dic[max_ - 1] += n
            n = 0
        else:
            dic[max_ - 1] += dic[max_]
            n -= dic[max_]
            del dic[max_]
        max_ -= 1
    
    for i in range(1, max(dic) + 1):
        result += i ** 2 * dic[i]
    
    return result