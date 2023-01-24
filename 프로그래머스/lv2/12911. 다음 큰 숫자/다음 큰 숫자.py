def solution(n):
    answer = n + 1
    num = format(n, 'b').count('1')
    print(num)
    while True:
        if format(answer, 'b').count('1') == num:
            break
        answer += 1
    return answer