def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        tmp = set(str(i))
        if (len(tmp) == 1 and '5' in tmp) or (len(tmp) == 2 and '5' in tmp and '0' in tmp):
            answer.append(i)
    return answer if len(answer) != 0 else [-1]