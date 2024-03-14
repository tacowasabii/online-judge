import math

def cal_fee(min, fees):
    if min <= fees[0]:
        return fees[1]
    return fees[1] + math.ceil((min - fees[0]) / fees[2]) * fees[3]

def toMin(n):
    h,m = n.split(":")
    return int(h)*60 + int(m)

def solution(fees, records):
    answer = []
    dic = {}
    dic2 = {}
    for i in records:
        time, num, inout = i.split(" ")
        if inout == "IN":
            dic[num] = toMin(time)
        elif inout == "OUT":
            dic2[num] = dic2.get(num,0) + toMin(time) - dic[num]
            del dic[num]
    if len(dic) > 0:
        for k, v in dic.items():
            dic2[k] = dic2.get(k,0) + toMin("23:59") - v
    dic2 = dict(sorted(dic2.items()))
    for v in dic2.values():
        answer.append(cal_fee(v, fees))

    return answer