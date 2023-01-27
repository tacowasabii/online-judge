import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:  #O(n)
        min1 = heapq.heappop(scoville)  #O(logn)
        if min1 >= K:
            break
        if len(scoville) == 1:
            return -1
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2 * min2  #O(logn)
        heapq.heappush(scoville, new_scoville)   #O(logn)
        answer += 1
    return answer

    #O(logn)