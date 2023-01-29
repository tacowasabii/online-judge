def solution(s):
    temp=[]
    for i in s:
        if not temp:
            temp.append(i)
        elif i==temp[-1]:
            temp.pop()
        else:
            temp.append(i)
    if len(temp)>0:
        return 0
    else:
        return 1