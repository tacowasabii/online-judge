def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    camera = routes[0][1]
    
    for i in routes:
        if i[0] > camera:
            answer += 1
            camera = i[1]
    return answer