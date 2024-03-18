import heapq

def solution(jobs):
    # 요청 시간 기준으로 정렬
    jobs.sort(reverse=True)
    n = len(jobs)
    heap = []  # 현재 처리할 수 있는 작업들
    time, answer = 0, 0
    
    # 모든 작업이 처리될 때까지 반복
    while jobs or heap:
        # 현재 시간 이전에 도착한 작업들을 힙에 추가
        while jobs and jobs[-1][0] <= time:
            job = jobs.pop()
            heapq.heappush(heap, (job[1], job[0]))  # (소요 시간, 요청 시간)으로 힙에 추가
        
        if heap:
            # 힙에서 가장 짧은 작업을 처리
            dur, start = heapq.heappop(heap)
            time += dur  # 현재 시간 업데이트
            answer += time - start  # 요청부터 종료까지 걸린 시간 추가
        else:
            # 현재 처리할 작업이 없으면 시간을 증가
            time += 1
    
    return answer // n  