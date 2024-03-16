def solution(board, h, w):
    answer = 0
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    
    row = len(board)
    col = len(board[0])
    
    color = board[h][w]
    for r, c in dirs:
        nr = h + r
        nc = w + c
        if 0 <= nr < row and 0 <= nc < col:
            if board[nr][nc] == color:
                answer += 1
    return answer