def solution(participant, completion):
    # 내 풀이
    a = dict.fromkeys(participant,0)
    for i in participant:
        a[i] += 1
    # 모범 풀이
    a = {}
    for i in participant:
        a[i] = a.get(i,0) + 1
        
    for i in completion:
        a[i] -= 1
    b = [k for k, v in a.items() if v == 1]
    
    return b[0]
