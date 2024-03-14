from collections import Counter

def solution(X, Y):
    answer = ''
    dic = {}
    
    xc = Counter(X)
    yc = Counter(Y)
    
    for i in xc:
        if i in yc:
            dic[i] = min(xc[i], yc[i])
    if len(dic) == 0:
        return "-1"
    
    a = sorted(dic,reverse = True)
    
    for i in a:
         answer += i * dic[i]
        
    return "0" if answer.lstrip("0") == "" else answer