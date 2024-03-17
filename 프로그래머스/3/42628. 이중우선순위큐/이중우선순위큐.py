import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for i in operations:
        command, value = i.split()
        value = int(value)
        
        if command == "I":
            heapq.heappush(min_heap,value)
            heapq.heappush(max_heap,-value)
        else:
            if value == 1 and max_heap:
                max_value = heapq.heappop(max_heap)
                min_heap.remove(-max_value)
            elif value == -1 and min_heap: 
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
    
    if min_heap:
        return [-max_heap[0],min_heap[0]]
    return [0,0] 