def solution(survey, choices):
    answer = ''
    dic = {}
    for i, v in enumerate(survey):
        choice = choices[i]
        if choice == 1:
            dic[v[0]] = dic.get(v[0],0) + 3
        elif choice == 2:
            dic[v[0]] = dic.get(v[0],0) + 2
        elif choice == 3:
            dic[v[0]] = dic.get(v[0],0) + 1
        elif choice == 5: 
            dic[v[1]] = dic.get(v[1],0) + 1
        elif choice == 6:
            dic[v[1]] = dic.get(v[1],0) + 2
        elif choice == 7:
            dic[v[1]] = dic.get(v[1],0) + 3
            
    per = [("R", "T"),("C", "F"),("J","M"),("A","N")]
    
    for i in per:
        if dic.get(i[0],0) >= dic.get(i[1],0):
            answer += i[0]
        else:
            answer += i[1]
    
    return answer