def solution(participant, completion):
    a = dict.fromkeys(participant,0)
    for i in participant:
        a[i] += 1
    for i in completion:
        a[i] -= 1
    b = [k for k, v in a.items() if v == 1]
    
    return b[0]
