from collections import deque as dq

def solution(order):
    boxes = dq([i for i in range(1, len(order) + 1)])
    order = dq(order)
    answer = 0
    sub = dq([])
    
    while len(order) > 0:
        tmp = order.popleft()
        if len(boxes) > 0 and tmp == boxes[0]:
            boxes.popleft()
            answer += 1
        elif len(sub) > 0 and tmp == sub[0]:
            sub.popleft()
            answer += 1
        elif len(boxes) == 0 and (len(sub) == 0 or sub[0] != tmp):
            break
        else:
            a = boxes.popleft()
            sub.appendleft(a)
            order.appendleft(tmp)
            
    return answer