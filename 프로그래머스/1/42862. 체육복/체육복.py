def solution(n, lost, reserve):
    cnt = 0
    tmp = lost.copy()
    lost.sort()
    reserve.sort()
    for i in tmp:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    left = []
    
    while lost and reserve:
        tmp = lost.pop(0)
        if (tmp - 1) in reserve:
            reserve.remove(tmp - 1)
        elif (tmp + 1) in reserve:
            reserve.remove(tmp + 1)
        else:
            left.append(tmp)
        
    return n - len(left) - len(lost)
