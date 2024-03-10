def solution(arr, n):
    answer = []
    if(len(arr) % 2 == 0):
        for i,v in enumerate(arr):
            if i % 2 != 0:
                answer.append(v+n)
            else:
                answer.append(v)
    else:
        for i,v in enumerate(arr):
            if i % 2 == 0:
                answer.append(v+n)
            else:
                answer.append(v)
    return answer