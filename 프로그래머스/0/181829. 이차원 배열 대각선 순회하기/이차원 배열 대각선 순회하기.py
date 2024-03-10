def solution(board, k):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                count += board[i][j]
    return count