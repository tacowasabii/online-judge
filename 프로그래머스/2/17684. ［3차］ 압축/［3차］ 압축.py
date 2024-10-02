def solution(msg):
    answer = []
    dic = {}
    
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = i - ord('A') + 1
    num = 27
    idx = 0
    
    while idx < len(msg):
        length = 1
        while msg[idx:idx + length] in dic:
            if idx + length == len(msg):
                answer.append(dic[msg[idx:idx + length]])
                return answer
            length += 1
        answer.append(dic[msg[idx:idx + length - 1]])
        dic[msg[idx:idx + length]] = num
        num += 1
        idx += length - 1
        
    return answer