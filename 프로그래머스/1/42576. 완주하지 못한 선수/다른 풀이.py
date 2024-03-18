from collections import Counter

# 객체끼리 빼기 가능
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]