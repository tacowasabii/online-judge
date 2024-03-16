def solution(sequence, k):
    start, end = 0, 0
    current_sum = 0
    min_length = float('inf')
    result = []

    while end < len(sequence):
        current_sum += sequence[end]
        
        while current_sum >= k and start <= end:
            if current_sum == k and (end - start + 1) < min_length:
                min_length = end - start + 1
                result = [start, end]  
            
            current_sum -= sequence[start]
            start += 1
            
        end += 1
    
    if min_length == float('inf'):
        return []  
    else:
        return result

