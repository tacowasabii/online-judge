def solution(n):
    count = 0
    a = 0
    while count < n:
        a += 1
        if '3' not in str(a) and a % 3 != 0:
            count += 1
    return a
