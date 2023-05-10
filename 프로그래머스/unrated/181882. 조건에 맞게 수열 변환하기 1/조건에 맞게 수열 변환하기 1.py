def solution(arr):
    answer=[]
    for i in arr:
        if i >= 50 and i%2==0:
            tmp=i//2
        elif i < 50 and i%2!=0:
            tmp=i*2
        else:
            tmp=i
        answer.append(tmp)
    return answer