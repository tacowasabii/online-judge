def solution(dartResult):
    answer = []
    
    num = ""
    for i in dartResult:
        if i.isnumeric():
            num += i
        else:
            if num:
                answer.append(int(num))
                num = ""
            if i == 'D':
                tmp = answer.pop()
                answer.append(tmp ** 2)
            elif i == 'T':
                tmp = answer.pop()
                answer.append(tmp ** 3)
            elif i == '*':
                tmp = answer.pop()
                if len(answer) >= 1:
                    tmp2 = answer.pop()
                    answer.append(tmp2 * 2)
                answer.append(tmp * 2)
            elif i == '#':
                tmp = answer.pop()
                answer.append(-tmp)
    
    return sum(answer)