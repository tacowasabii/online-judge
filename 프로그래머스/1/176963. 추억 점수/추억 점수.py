def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i, v in enumerate(name):
        dic[v] = yearning[i]
    for j in photo:
        score = 0
        for k in j:
            score += dic.get(k,0)
        answer.append(score)
    return answer