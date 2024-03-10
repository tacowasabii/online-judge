def solution(n):
    if n == 1:
        return [[1]]
    matrix = [[0] * n for _ in range(n)]
    dir = [(0,1), (1,0), (0,-1), (-1,0)]
    cur_dir = 0
    row = 0
    col = 0
    for i in range(1, n**2 + 1):
        matrix[row][col] = i
        row += dir[cur_dir][0]
        col += dir[cur_dir][1]
        
        if cur_dir == 0 and col == n-1:
            cur_dir = 1
        elif cur_dir == 0 and matrix[row][col+1] != 0:
            cur_dir = 1
        elif cur_dir == 1 and row == n-1:
            cur_dir = 2
        elif cur_dir == 1 and matrix[row+1][col] != 0:
            cur_dir = 2
        elif cur_dir == 2 and col == 0:
            cur_dir = 3
        elif cur_dir == 2 and matrix[row][col-1] != 0:
            cur_dir = 3
        elif cur_dir == 3 and row == 0:
            cur_dir = 0
        elif cur_dir == 3 and matrix[row-1][col] != 0:
            cur_dir = 0
    return matrix