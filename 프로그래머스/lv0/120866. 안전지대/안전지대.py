def solution(board):
    answer = 0
    a = []
    for i in range(len(board) + 2):
        a.append([0 for i in range(len(board) + 2)])

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        a[i + k + 1][j + l + 1] = 1
    
    a = a[1:-1]
    for j in range(len(a)):
        a[j] = a[j][1:-1]

    
    for i in a:
        answer += i.count(0)

    return answer



