from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    
    # 양방향 그래프 구성
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 방문 여부와 각 노드까지의 거리를 저장할 딕셔너리
    distances = {node: 0 for node in range(1, n+1)}
    visited = set([1])
    
    queue = deque([(1, 0)])  # (노드 번호, 거리)
    
    # BFS 실행
    while queue:
        current_node, distance = queue.popleft()
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distance + 1
                queue.append((neighbor, distance + 1))
    
    # 가장 긴 최단 경로 찾기
    max_distance = max(distances.values())
    answer = list(distances.values()).count(max_distance)
    
    return answer

# distance를 따로 관리함
