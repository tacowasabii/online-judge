def solution(board, moves):
    answer = 0
    stack = []
    
    depth = len(board)
    for i in moves:
        tmp = 0
        for j in range(depth):
            if board[j][i-1] != 0:
                tmp = board[j][i-1]
                board[j][i-1] = 0
                break
        if tmp != 0:
            stack.append(tmp)
        
        while True:
            if len(stack) <= 1:
                break
            else:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                else:
                    break

    return answer