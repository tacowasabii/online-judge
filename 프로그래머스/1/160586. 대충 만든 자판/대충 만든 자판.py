def solution(keymap, targets):
    answer = []
    dic = {}
    for i in keymap:
        for idx, j in enumerate(i):
            dic[j] = min(dic.get(j, 101), idx + 1)
    for i in targets:
        cnt = 0
        for j in i:
            if j not in dic:
                cnt = -1
                break
            else:
                cnt += dic[j]
        answer.append(cnt)
    return answer