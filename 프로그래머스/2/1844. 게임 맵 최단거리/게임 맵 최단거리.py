from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    queue = deque([[0, 0]])
    maps[0][0] = 2
    
    while queue:
        r, c = queue.popleft()
        
        if r == row - 1 and c == col - 1:
            return maps[r][c] - 1
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1
                queue.append([nr, nc])
    
    return -1 