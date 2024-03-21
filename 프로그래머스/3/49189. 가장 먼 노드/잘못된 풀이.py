# 예제는 통과했으나 제출에서 틀림
# bfs로 풀어야 하는데 dfs로 풀었음

from collections import defaultdict

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    
    stack = [(1,0)]
    result = []
    maxlen = 0
    while stack:
        tmp = stack.pop()
        result.append(tmp)
        visited.add(tmp[0])
        for i in graph[tmp[0]]:
            if i not in visited:
                stack.append((i, tmp[1] + 1))
                maxlen = max(maxlen, tmp[1] + 1)
                visited.add(i)
            graph[tmp] = []
    for i in result:
        if i[1] == maxlen:
            answer += 1
    
    return answer