def solution(n, m, section):
    point = 0
    ans = 0
    for i in section:
        if i > point:
            point = i + m - 1
            ans += 1
    return ans