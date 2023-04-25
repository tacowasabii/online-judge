def solution(numLog):
    answer = ''
    for i in range(len(numLog) - 1):
        n = numLog[i + 1] - numLog[i]
        if n == 1:
            answer += 'w'
        elif n == -1:
            answer += 's'
        elif n == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer