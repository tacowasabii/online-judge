def solution(s):
    answer = ''
    a=sorted(set(list(s)))
    for i in a:
        count=0
        for j in s:
            if i==j:
                count+=1
        if count==1:
            answer+=i
    return answer