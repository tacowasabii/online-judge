def solution(k, dungeons):
    ans = [0]
    def explore(k, dungeons, count):
        ans[0] = max(ans[0], count)
        for i, v in enumerate(dungeons):
            if k >= v[0]:
                explore(k - v[1], dungeons[:i]+dungeons[i+1:], count + 1)
    explore(k, dungeons, 0)
    return ans[0]