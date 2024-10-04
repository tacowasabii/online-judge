def solution(skill, skill_trees):
    answer = 0
    dic = {}
    for i in range(len(skill)):
        dic[skill[i]] = i

    for i in skill_trees:
        level = -1
        flag = True
        for j in i:
            if j in dic:
                if 0 <= dic[j] - level <= 1:
                    level = dic[j]
                else:
                    flag = False
                    break
        if flag:
            answer += 1
        
    return answer