def solution(arr, flag):
    answer = []
    for i,v in enumerate(flag):
        if v:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
            
    return answer