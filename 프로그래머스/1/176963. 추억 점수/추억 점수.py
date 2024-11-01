def solution(name, yearning, photo):
    result = []
    dic = {}
    for i, v in enumerate(name):
        dic[v] = yearning[i]
    for i in photo:
        score = 0
        for j in i:
            score += dic.get(j, 0)
        result.append(score)
    return result 