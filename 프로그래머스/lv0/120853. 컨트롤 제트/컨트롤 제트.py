def solution(s):
    answer = 0
    a=s.split()
    b=0
    for i in a:
        if i!='Z':
            answer+=int(i)
            b=i
        else:
            answer-=int(b)
    return answer