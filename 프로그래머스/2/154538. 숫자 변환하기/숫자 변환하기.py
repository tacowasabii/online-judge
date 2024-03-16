def solution(x, y, n):
    answer = 0
    
    tmp = set([x])
    cnt = 0
    
    if x == y:
        return 0
    
    while True:
        a = set()
        for i in tmp:
            a.add(i + n)
            a.add(i * 2)
            a.add(i * 3)
        cnt += 1
        if y in a:
            return cnt
        elif min(a) > y:
            return -1
        
        tmp = a
        
    return answer