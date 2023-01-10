def solution(keyinput, board):
    answer = [0, 0]
    x = 0
    y = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    xl = board[0] // 2
    yl = board[1] // 2
    dir = ["up", "down", "left", "right"]
    for i in keyinput:
        idx = dir.index(i)
        x += dx[idx]
        y += dy[idx]
        if xl >= x >= -xl:
            answer[0] = x
        else:
            x -= dx[idx]
        if yl >= y >= -yl:
            answer[1] = y
        else:
            y -= dy[idx]
    return answer
