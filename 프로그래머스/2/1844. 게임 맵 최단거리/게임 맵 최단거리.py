from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    
    def isValid(x, y):
        if 0 <= x <= n-1 and 0 <= y <= m-1 and maps[x][y] == 1:
            return True
        
    dq = deque([(0,0)])
    maps[0][0] = 2 
    
    while dq:
        x, y = dq.popleft()
        if x == n-1 and y == m-1:
            return maps[x][y] - 1
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if isValid(nx,ny):
                maps[nx][ny] = maps[x][y] + 1
                dq.append((nx,ny))
    
    return -1 