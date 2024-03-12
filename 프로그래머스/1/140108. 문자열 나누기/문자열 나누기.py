def solution(s):
    answer = 0
    isStart = True
    tmp = ''
    c1 = 0
    c2 = 0
    for i in s:
        if isStart:
            tmp = i
            c1 += 1
            isStart = False
        else:
            if i == tmp:
                c1 += 1
            else:
                c2 += 1
            if c1 == c2:
                answer += 1
                c1, c2 = 0, 0
                isStart = True
    if not isStart:
        answer += 1
    return answer