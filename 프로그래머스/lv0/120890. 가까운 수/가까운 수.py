def solution(array, n):
    answer = []
    b=[]
    for i in array:
        b.append(abs(i-n))
    for j,k in enumerate(b):
        if k==min(b):
            answer.append(array[j])
    return min(answer)