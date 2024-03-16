def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 != 0: 
        return -1
    target = total_sum // 2
    len_q1, len_q2 = len(queue1), len(queue2)
    idx1, idx2, current_sum, count = 0, len_q1, sum(queue1), 0
    queue = queue1 + queue2 + queue1  

    while idx1 < len_q1+len_q2 and idx2 < len_q1*2+len_q2:
        if current_sum == target:
            return count
        elif current_sum < target:
            current_sum += queue[idx2]
            idx2 += 1
            count += 1
        else:
            current_sum -= queue[idx1]
            idx1 += 1
            count += 1

    return -1
