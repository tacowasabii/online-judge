def solution(elements):
    result = set()
    length = len(elements)
    elements += elements
    for i in range(length):
        for j in range(1, length + 1):
            result.add(sum(elements[i:i + j]))
        
    return len(result)