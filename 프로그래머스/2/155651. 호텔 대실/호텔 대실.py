from heapq import heapify, heappush, heappop

def parse_time(time):
    h, m = time.split(":")
    
    return int(h) * 60 + int(m)

def solution(book_time):
    book_time.sort(key = lambda x:x[0])
    rooms = [0]
    heapify(rooms)
    
    for s, e in book_time:
        a = heappop(rooms)
        if a > parse_time(s):
            heappush(rooms, a)
        heappush(rooms, parse_time(e) + 10)
        
    return len(rooms)