def solution(lines):
    answer = 0
    a = []
    for i in lines:
        b = list(range(i[0], i[1]))
        a += b

    for i in set(a):
        if a.count(i) >= 2:
            answer += 1
            
    return answer