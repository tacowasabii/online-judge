def solution(n, computers):
    ans = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            ans += 1
            stack = [i]
            while stack:
                point = stack.pop()
                visited[point] = 1
                for j, v in enumerate(computers[point]):
                    if visited[j] == 0 and v == 1:
                        stack.append(j)
        
    return ans