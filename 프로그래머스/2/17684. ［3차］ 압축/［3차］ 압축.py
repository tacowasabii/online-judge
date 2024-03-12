def solution(msg):
    answer = []
    dic = {}
    cnt = 1
    for i in range(ord('A'),ord('Z')+1):
        dic[chr(i)] = cnt
        cnt += 1
    idx = 0
    while idx < len(msg):
        i = idx
        v = msg[i]
        while True:
            if v in dic and i != len(msg)-1:
                v += msg[i+1]
                i += 1
                idx += 1
            else:
                break
        if v in dic:
            answer.append(dic[v])
            idx += 1
        else:
            answer.append(dic[v[:-1]])
            dic[v] = cnt
            cnt += 1
        
    return answer