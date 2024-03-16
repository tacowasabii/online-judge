def num(n):
    n2 = bin(n)
    if n2[-1] == '0':
        return int(n2[:-1]+'1',2)
    else:
        tmp = list(n2[::-1])
        tmp = tmp[:-2] + ['0'] + tmp[-2:]

        for i, v in enumerate(tmp):
            if v == '0':
                tmp[i] = '1'
                tmp[i-1] = '0'
                a = ''
                a = a.join(tmp)
                return int(a[::-1],2)
                

def solution(numbers):
    answer = []
    
    for i in numbers:
        answer.append(num(i))
            
    return answer