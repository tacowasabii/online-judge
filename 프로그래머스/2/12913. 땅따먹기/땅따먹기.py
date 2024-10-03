def solution(land):
    
    for i in range(len(land) - 1):
        tmp = sorted(land[i], reverse = True)
        max_idx = land[i].index(tmp[0])
        for j in range(4):
            if j != max_idx:
                land[i + 1][j] += tmp[0]
            else:
                land[i + 1][j] += tmp[1]
    return max(land[-1])
            