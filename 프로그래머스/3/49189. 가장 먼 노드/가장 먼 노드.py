from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set([1])
    
    queue = deque([(1,0)])
    result = []
    maxlen = 0
    while queue:
        tmp = queue.popleft()
        result.append(tmp)

        for i in graph[tmp[0]]:
            if i not in visited:
                queue.append((i, tmp[1] + 1))
                maxlen = max(maxlen, tmp[1] + 1)
                visited.add(i)
    for i in result:
        if i[1] == maxlen:
            answer += 1
    
    return answer