def solution(dirs):
    answer = 0
    paths = []
    cur = (0,0)
    dic = {'U':(0, 1), "D":(0, -1), "R":(1, 0), "L":(-1, 0)}
    
    for i in dirs:
        nx = cur[0] + dic[i][0]
        ny = cur[1] + dic[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if [cur, (nx, ny)] not in paths:
                answer += 1
                paths += [[cur, (nx, ny)], [(nx, ny), cur]]
            cur = (nx, ny)
    
    return answer