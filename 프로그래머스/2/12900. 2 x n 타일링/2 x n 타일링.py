from math import comb

def solution(n):
    if n == 0 or n == 1:
        return 1
    
    prev, cur = 1, 1
    
    for _ in range(2, n + 1):
        prev, cur = cur, (prev + cur) % 1000000007
    
    return cur
    