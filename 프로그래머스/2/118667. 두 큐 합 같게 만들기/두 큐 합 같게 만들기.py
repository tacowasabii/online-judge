def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 != 0: 
        return -1
    
    idx1, idx2 = 0, len(queue1)
    queue = queue1 + queue2 + queue1
    sum1, sum2 = sum(queue1), sum(queue2)
    cnt = 0
    
    while idx1 < len(queue1) + len(queue2) and idx2 < len(queue):
        if sum1 == total_sum / 2:
            return cnt
        elif sum1 < sum2:
            sum1 += queue[idx2]
            sum2 -= queue[idx2]
            idx2 += 1
            cnt += 1
        elif sum1 > sum2:
            sum1 -= queue[idx1]
            sum2 += queue[idx1]
            idx1 += 1
            cnt += 1
            
    return -1
