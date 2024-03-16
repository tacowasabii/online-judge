def check(m, n, board):
    to_erase = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != '0' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                to_erase |= {(i, j), (i+1, j), (i, j+1), (i+1, j+1)}
    return to_erase

def erase(board, to_erase, n, m):
    for i, j in to_erase:
        board[i][j] = '0'
    
    for i in range(n):
        tmp = ''
        for j in range(m):
            if board[j][i] != '0':
                tmp += board[j][i]
        new = '0' * (m - len(tmp)) + tmp
        for j in range(m):
            board[j][i] = new[j]
    
    return board        

def solution(m, n, board):
    answer = 0
    board = list(map(list, board)) 

    while True:
        to_erase = check(m,n,board)
        if not to_erase:
            break
        erase(board, to_erase, n ,m)
    
    for i in board:
        for j in i:
            if j == '0':
                answer += 1
    
    return answer