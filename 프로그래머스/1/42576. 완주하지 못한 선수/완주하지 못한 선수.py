from collections import Counter

def solution(participant, completion):
    part = Counter(participant)
    compl = Counter(completion)
    
    for i in compl:
        part[i] -= compl[i]
    
    for i in part:
        if part[i] > 0:
            return i