def solution(n, lost, reserve):
    a = []
    for i in range(n):
        a.append(1)
    for i in lost:
        a[i - 1] -= 1
    for i in reserve:
        a[i - 1] += 1
    for i in range(n - 1):
        if a[i] == 0 and a[i + 1] == 2:
            a[i] += 1
            a[i + 1] -= 1
        if a[i] == 2 and a[i + 1] == 0:
            a[i] -= 1
            a[i + 1] += 1
    return a.count(1)+a.count(2)