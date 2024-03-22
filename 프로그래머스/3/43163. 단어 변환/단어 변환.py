from collections import deque as dq

def can_transform(a, b):
    tmp = [1 for i, j in zip(a, b) if i!=j]
    
    return sum(tmp) == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = dq([[begin, 0]])
    
    while queue:
        word, cnt = queue.popleft()
        
        for i in words:
            if can_transform(word, i):
                if i == target:
                    return cnt + 1
                queue.append([i, cnt + 1])
    
    return 0