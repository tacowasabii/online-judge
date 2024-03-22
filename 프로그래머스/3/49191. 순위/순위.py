def solution(n, results):
    cnt = 0
    win = {x: set() for x in range(1, n+1)}
    lose = {x: set() for x in range(1, n+1)}
    
    for a, b in results:
        win[a].add(b)
        lose[b].add(a)
    
    for i in range(1, n + 1):
        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[i])
    
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            cnt += 1
    
    return cnt
