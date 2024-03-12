from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    cnt = 0
    while True:
        a = queue.popleft()
        if len(queue) == 0:
            return cnt + 1
        if a < max(queue):
            queue.append(a)
            if location == 0:
                location += len(queue) - 1
            else:
                location -= 1
        else:
            if location == 0:
                return cnt + 1
            else:
                location -= 1
                cnt += 1