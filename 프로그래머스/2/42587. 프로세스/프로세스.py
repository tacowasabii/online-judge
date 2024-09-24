from collections import deque

def solution(priorities, location):
    order = 0
    priorities = deque(priorities)
    while location >= 0:
        tmp = priorities.popleft()
        location -= 1
        if priorities and tmp < max(priorities):
            priorities.append(tmp)
            if location == -1:
                location = len(priorities) - 1
        else:
            order += 1
    return order            
                