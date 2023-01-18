def solution(chicken):
    a = chicken // 10 + chicken % 10
    
    if a < 10:
        return chicken // 10

    return chicken // 10 + solution(a)