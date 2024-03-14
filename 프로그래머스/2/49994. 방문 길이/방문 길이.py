def solution(dirs):
    answer = 0
    paths = []
    cur = (0,0)
    dir = {"L":(-1,0), "R":(1,0), "U":(0,1), "D":(0,-1)}
    
    for i in dirs:
        nx = cur[0] + dir[i][0]
        ny = cur[1] + dir[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = (cur,(nx,ny))
            if path not in paths:
                answer += 1
                paths += [(cur,(nx,ny)),((nx,ny),cur)]
            cur = (nx,ny)
    return answer