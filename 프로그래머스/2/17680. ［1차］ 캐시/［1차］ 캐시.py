from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for i in cities:
        i = i.lower()
        if i in cache:
            answer += 1
            cache.remove(i)
        else:
            answer += 5
            if cache and len(cache) == cacheSize:
                cache.popleft()
        if cacheSize > 0:
            cache.append(i)
    return answer