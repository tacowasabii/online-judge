from collections import Counter

def solution(k, tangerine):
    ans = 0
    oranges = sorted(Counter(tangerine).values(), reverse = True)

    for i in oranges:
        k -= i
        ans += 1
        if k <= 0:
            return ans