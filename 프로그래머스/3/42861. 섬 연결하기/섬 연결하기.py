def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # 비용을 기준으로 오름차순 정렬
    parent = [i for i in range(n)]  # 부모 테이블 초기화

    answer = 0
    for a, b, cost in costs:
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer
