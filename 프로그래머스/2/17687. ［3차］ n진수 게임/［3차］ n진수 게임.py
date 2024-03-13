def toN(t, n):
    N = ''
    while t >= n:
        tmp = t % n
        if tmp == 10:
            tmp = 'A'
        elif tmp == 11:
            tmp = 'B'
        elif tmp == 12:
            tmp = 'C'
        elif tmp == 13:
            tmp = 'D'
        elif tmp == 14:
            tmp = 'E'
        elif tmp == 15:
            tmp = 'F'
        N += str(tmp)
        t = t // n
    if t == 10:
        t = 'A'
    elif t == 11:
        t = 'B'
    elif t == 12:
        t = 'C'
    elif t == 13:
        t = 'D'
    elif t == 14:
        t = 'E'
    elif t == 15:
        t = 'F'
    N += str(t)
    
    return N[::-1]

def solution(n, t, m, p):
    answer = ''
    tmp = ''
    length = p + m * (t - 1)
    cnt = 0
    print(toN(11,16))
    while len(tmp) <= length:
        tmp += toN(cnt, n)
        cnt += 1
    for i in range(p-1, length, m):
        answer += tmp[i]
    return answer