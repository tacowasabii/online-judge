from collections import deque as dq

def solution(bridge_length, weight, truck_weights):
    finished = []
    time = 0
    trucks = dq(truck_weights)
    bridge = dq([0] * bridge_length)
    weights = 0
    while len(finished) != len(truck_weights):
        tmp = bridge.pop()
        if tmp != 0:
            finished.append(tmp)
            weights -= tmp
        new = 0
        if len(trucks) > 0:
            if trucks[0] + weights <= weight:
                new = trucks.popleft()
                weights += new
        bridge.appendleft(new)
        time += 1
                
    return time