def solution(keyinput, board):
    answer = [0, 0]
    x, y = 0,0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    xl = board[0] // 2
    yl = board[1] // 2
    dir = ["up", "down", "left", "right"]
    for i in keyinput:
        idx = dir.index(i)
        if xl >= x+dx[idx] >= -xl:
            x += dx[idx]
        if yl >= y+dy[idx] >= -yl:
            y += dy[idx]
    return [x,y]
