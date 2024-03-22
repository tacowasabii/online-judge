from collections import deque as dq

# 무한 루프가 되고 답이 없는 경우가 없어서 통과했는데
# 무한 루프가 되는 경우가 있을 수 있음
# 그래서 방문한 노드를 체크해야 함
# 그래프 탐색 알고리즘에서는 방문한 노드를 체크하는 것이 중요함
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