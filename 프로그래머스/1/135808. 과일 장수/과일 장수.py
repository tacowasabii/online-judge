def solution(k, m, score):
    answer = 0
    if len(score) < m:
        return 0
    score.sort(reverse = True)
    for i in range(len(score) // m):
        arr = score[i * m:(i + 1) * m]
        answer += min(arr) * m
    return answer