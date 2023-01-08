def solution(n):
    answer = []
    a=[]
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            a.append(i)
    for k in a:
        if n%k==0:
            answer.append(k)
    return answer