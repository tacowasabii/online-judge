def solution(numbers):
    answer = 0
    for a,i in enumerate(numbers):
        for b,j in enumerate(numbers):
            if a!=b:
                answer=max(answer,i*j)
    return answer