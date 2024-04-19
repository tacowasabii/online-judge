def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    a, b = 0, 0
    
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            a += 1
            b += 1
            answer += 1
        else:
            a += 1
    
    return answer