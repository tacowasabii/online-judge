def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        tmp = i
        for j in i:
            if j not in skill:
                tmp = tmp.replace(j, '')
        if skill.startswith(tmp):
            answer += 1
        
    return answer