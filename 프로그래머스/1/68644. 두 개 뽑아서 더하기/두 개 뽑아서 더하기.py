from itertools import combinations

def solution(numbers):
    idx = [i for i in range(len(numbers))]
    combs = combinations(idx, 2)
    result = set()
    for comb in combs:
        result.add(numbers[comb[0]] + numbers[comb[1]])
    return sorted(list(result))