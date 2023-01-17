def solution(number, k):
    answer = ''
    a=[0]
    b = list(number)
    count=0
    for i in b:
        a.append(int(i))
        while min(a)<int(i) and count<=k:
            if min(a)<int(i):
                a.pop(a.index(min(a)))
                count += 1
    count-=1
    if count<k:
        a=a[:count-k]
    return answer.join(map(str,a))

# 로직은 맞는데 시간 초과