def solution(dartResult):
    answer = []
    num = ""
    for i in dartResult:
        if i.isnumeric():
            num += i
        else:
            if len(num) > 0:
                answer.append(int(num))
                num = ""
            if i == 'D':
                answer[-1] = answer[-1] ** 2
            elif i == 'T':
                answer[-1] = answer[-1] ** 3
            elif i == '*':
                answer[-1] *= 2
                if len(answer) >= 2:
                    answer[-2] *= 2
            elif i == '#':
                answer[-1] = -answer[-1]
            
    return sum(answer)