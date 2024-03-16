def solution(n):
    answer = ''
    length = 1
    cnt = 0
    
    nums = ['1','2','4']
    while n > cnt:
        n -= cnt
        cnt = 3 ** length
        length += 1
    
    length -= 1
    for _ in range(length):
        answer += nums[(n-1) // 3 ** (length - 1)]
        n -= ((n-1) // 3 ** (length - 1)) * 3 ** (length - 1)
        length -= 1
        
    
    return answer