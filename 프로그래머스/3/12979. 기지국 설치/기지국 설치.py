from math import ceil

def solution(n, stations, w):
    answer = 0
    cover_range = 2 * w + 1
    idx = 1
    for i in stations:
        if idx < i - w:
            answer += ceil((i-w-idx)/cover_range)
        idx = i + w + 1
    if idx <= n:
        answer += ceil((n-idx+1)/cover_range)
    return answer