import math

def toMinute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def calFee(fees, time):
    dt, df, um, uf = fees
    
    if time <= dt:
        return df
    else:
        return df + math.ceil((time - dt) / um) * uf

def solution(fees, records):
    answer = []
    dic = {}
    dic2 = {}

    for record in records:
        time, number, info = record.split()
        if info == "IN":
            dic[number] = toMinute(time)
        else:
            dic2[number] = dic2.get(number, 0) + (toMinute(time) - dic[number])
            dic[number] = -1

    for k, v in dic.items():
        if v != -1:
            dic2[k] = dic2.get(k, 0) + (toMinute("23:59") - v)
    
    dic2 = dict(sorted(dic2.items()))
    
    for v in dic2.values():
        answer.append(calFee(fees, v))
    
    return answer