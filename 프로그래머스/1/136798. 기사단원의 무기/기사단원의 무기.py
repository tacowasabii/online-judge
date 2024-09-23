def nums(num):
    cnt = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt += 2
    if num ** 0.5 == int(num ** 0.5):
        cnt -= 1
    return cnt

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        if nums(i) > limit:
            answer += power
        else:
            answer += nums(i)
    return answer