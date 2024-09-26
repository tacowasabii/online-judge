def toN(num, n):
    if num == 0:
        return '0'
    tmp = []
    while num > 0:
        tmp.append(num % n)
        num //= n
    tmp = tmp[::-1]
    
    result = ''
    for i in tmp:
        if i == 10:
            result += 'A'
        elif i == 11:
            result += 'B'
        elif i == 12:
            result += 'C'
        elif i == 13:
            result += 'D'
        elif i == 14:
            result += 'E'
        elif i == 15:
            result += 'F'
        else:
            result += str(i)
    return result

def solution(n, t, m, p):
    answer = ''
    string = ''
    num = 0
    while len(string) < m * (t - 1) + p:
        string += toN(num, n)
        num += 1

    for i in range(p - 1, m * (t - 1) + p, m):
        answer += string[i]
    return answer