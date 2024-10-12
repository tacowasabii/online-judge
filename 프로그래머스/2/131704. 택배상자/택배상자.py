from collections import deque as dq

def solution(order):
    ans = 0
    idx = 0
    boxes = dq([i for i in range(1, len(order) + 1)])
    sub = dq([0])
    
    while idx < len(order):
        if len(boxes) == 0 and order[idx] != sub[0]:
            break
        if boxes and boxes[0] == order[idx]:
            boxes.popleft()
            idx += 1
            ans += 1
        elif sub[0] == order[idx]:
            sub.popleft()
            idx += 1
            ans += 1
        else:
            sub.appendleft(boxes.popleft())
            
    return ans