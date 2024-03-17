from itertools import combinations as cb
from collections import Counter

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(orders[i]))

    for i in course:
        combination_counts = Counter()
        for order in orders:
            combination_orders = cb(order,i)
            combination_counts.update(combination_orders)
        
        if combination_counts:
            maxv = max(combination_counts.values())
            for comb, count in combination_counts.items():
                if count > 1 and count == maxv:
                    answer.append(''.join(comb))
            
    return sorted(answer)