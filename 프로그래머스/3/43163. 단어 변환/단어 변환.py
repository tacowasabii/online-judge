from collections import deque as dq

def can_transform(a, b):
    return sum([1 for i, j in zip(a, b) if i != j]) == 1
    

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = dq([(begin, 0)])
    while queue:
        tmp = []
        start, cnt = queue.popleft()
        if start == target:
            return cnt 
        
        for i in words:
            if can_transform(start, i):
                queue.append((i, cnt + 1))
            else:
                tmp.append(i)
        words = tmp
    
    return 0