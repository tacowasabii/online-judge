import math

def solution(num, total):
    answer = []
    a = math.floor(total / num) + 1
    b = math.floor(total / num - 0.5)
    if num % 2 == 1:
        answer.append(total / num)
    for i in range(a, a + num // 2):
        answer.append(i)
    for i in range(b, b - num // 2, -1):
        answer.insert(0,i)

    return answer