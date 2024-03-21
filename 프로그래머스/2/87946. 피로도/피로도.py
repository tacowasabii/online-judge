def solution(k, dungeons):
    answer = [0]
    
    def explore(k, dungeons, num):
        for i, v in enumerate(dungeons):
            if k >= v[0]:
                answer[0] = max(answer[0], num + 1)
                explore(k - v[1], dungeons[:i]+dungeons[i+1:], num + 1)
    
    explore(k, dungeons, 0)
    
    return answer[0]
        