def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i, v in enumerate(arr1):
        for j in range(len(arr2[0])):
            tmp = 0
            for i2, v2 in enumerate(v):
                tmp += v2 * arr2[i2][j]
            answer[i][j] = tmp
            
    return answer