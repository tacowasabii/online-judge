def solution(arr, k):
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
    for i in range(k):
        a.append(-1)
    return a[:k]