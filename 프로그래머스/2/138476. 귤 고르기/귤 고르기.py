from collections import Counter

def solution(k, tangerine):
    answer = 0
    fruits = Counter(tangerine)
    nums = list(fruits.values())
    nums.sort()
    
    total = 0
    while total < k:
        total += nums.pop()
        answer += 1
    return answer