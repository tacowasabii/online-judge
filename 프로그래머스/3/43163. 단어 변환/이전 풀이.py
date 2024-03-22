from collections import deque

def can_transform(a, b):
    diff_cnt = sum(1 for i, j in zip(a,b) if i != j)
    
    return diff_cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin,0)])
    visited = set()
    
    while queue:
        cur_word, step = queue.popleft()
        
        if cur_word == target:
            return step
        
        for word in words:
            if word not in visited and can_transform(cur_word, word):
                visited.add(word)
                queue.append((word,step + 1))
    
    return 0