def solution(triangle):
    answer = 0
    
    for i in range(len(triangle) - 1):
        for j, v in enumerate(triangle[i]):
            if j == 0:
                triangle[i + 1][0] += triangle[i][0]
            if j != i:
                triangle[i + 1][j + 1] += max(triangle[i][j], triangle[i][j + 1])
            if j == i:
                triangle[i + 1][i + 1] += triangle[i][i]
                
    return max(triangle[-1])    