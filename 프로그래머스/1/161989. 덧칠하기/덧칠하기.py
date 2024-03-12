def solution(n, m, section):
    answer = 1
    start = section[0]
    for i in section:
        if i >= start + m:
            answer += 1
            start = i
    return answer