def solution(n):
    answer = []
    
    tmp = [[0] * i for i in range(1, n + 1)]
    
    dirs = [(1,0),(0,1),(-1,-1)]
    
    a = 0
    x, y = -1, 0
    cnt = 1
    while n > 0:
        dir = dirs[a % 3]
        for _ in range(n):
            x += dir[0]
            y += dir[1]
            tmp[x][y] = cnt
            cnt += 1
        n -= 1
        a += 1
    
    for i in tmp:
        for j in i:
            answer.append(j)
    return answer