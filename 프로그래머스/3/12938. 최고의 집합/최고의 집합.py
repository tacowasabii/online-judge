def solution(n, s): 
    if s < n:
        return [-1]
    a, b = divmod(s, n)
    
    result = [a] * n
    
    for i in range(b):
        result[i] += 1
        
    return sorted(result)