def solution(array):
    a=0
    b=0
    for i in array:
        count=0
        for j in array:
            if i==j:
                count+=1
        if a<count:
            a=count
            b=i
        elif i!=b and a==count:
            b=-1
    return b