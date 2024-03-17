def solution(triangle):
    answer = 0
    
    for i, v in enumerate(triangle):
        for i2, v2 in enumerate(v):
            if i > 0:
                if i2 == 0:
                    triangle[i][i2] += triangle[i-1][i2]
                elif 0 < i2 < len(triangle[i]) - 1:
                    triangle[i][i2] += max(triangle[i-1][i2-1],triangle[i-1][i2])
                else:
                    triangle[i][i2] += triangle[i-1][i2-1]
    return max(triangle[-1])