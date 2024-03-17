from collections import Counter

def solution(n, works):
    answer = 0
    max_work = max(works)
    works_counter = Counter(sorted(works, reverse = True))

    while max_work > 0 and n > 0:
        max_n = works_counter[max_work]
        if max_n >= n:
            if max_work == 1:
                return max_n - n
            else:
                works_counter[max_work] -= n
                works_counter[max_work-1] += n
                break
        else:
            if max_work == 1:
                return 0
            else:
                works_counter[max_work-1] += works_counter[max_work]
                n -= works_counter[max_work]
                del works_counter[max_work]
        max_work -= 1
        
    for k, v in works_counter.items():
        answer += k ** 2 * v
                
    return answer