import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        order, num = operation.split(" ")
        
        if order == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        elif order == "D" and len(min_heap) > 0:
            if num == '1':
                v = heapq.heappop(max_heap)
                min_heap.remove(-v)
            elif num == '-1':
                v = heapq.heappop(min_heap)
                max_heap.remove(-v)
    if min_heap:
        return [-max_heap[0], min_heap[0]]
    
    return [0, 0]