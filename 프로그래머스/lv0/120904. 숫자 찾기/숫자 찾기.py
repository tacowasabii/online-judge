def solution(num, k):
    for i,j in enumerate(str(num)):
        if j==str(k):
            return i+1
    else:
        return -1
