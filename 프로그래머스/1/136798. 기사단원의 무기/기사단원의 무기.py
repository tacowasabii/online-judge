def getDivisorNum(n):
    num = 0
    
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            num += 1
            if i ** 2 != n:
                num +=1
    return num

def solution(number, limit, power):
    answer = 0
    tmp = []
    for i in range(1, number+1):
        tmp.append(getDivisorNum(i))
    for i, v in enumerate(tmp):
        if v > limit:
            tmp[i] = power
            
    return sum(tmp)