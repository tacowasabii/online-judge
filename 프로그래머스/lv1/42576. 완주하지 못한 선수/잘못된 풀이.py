def solution(participant, completion):
    if len(set(participant))!=len(set(completion)):
        a = list(set(participant)-set(completion))
        return a[0]
    for i in list(set(participant)):
        if participant.count(i)!=completion.count(i):
            return i

# 중첩 반복문으로 인한 시간초과
