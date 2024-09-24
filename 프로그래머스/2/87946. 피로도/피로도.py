def solution(k, dungeons):
    answer = [0]
    
    def explore(dungeons, blood, num):
        for i in range(len(dungeons)):
            if blood >= dungeons[i][0]:
                answer[0] = max(answer[0], num + 1)
                explore(dungeons[:i] + dungeons[i + 1:], blood - dungeons[i][1], num + 1)
    explore(dungeons, k, 0)
    
    return answer[0]
        