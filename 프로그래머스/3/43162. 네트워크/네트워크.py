def solution(n, computers):
    visited = [0] * n
    network_count = 0
    
    for i in range(n):
        if visited[i] == 0:
            stack = [i]
            
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = 1
                    for j, v in enumerate(computers[node]):
                        if v == 1 and not visited[j]:
                            stack.append(j)
            network_count += 1
    
    return network_count
