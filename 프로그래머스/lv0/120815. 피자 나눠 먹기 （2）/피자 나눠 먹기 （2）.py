def solution(n):
    count=1
    while(1):
        if (6*count)%n==0:
            break
        count+=1
    return count