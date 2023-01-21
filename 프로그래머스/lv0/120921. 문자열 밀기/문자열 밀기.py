def solution(A, B):
    B = B * 2
    if A == B:
        return 0
    elif A in B:
        return B.find(A)
    else:
        return -1