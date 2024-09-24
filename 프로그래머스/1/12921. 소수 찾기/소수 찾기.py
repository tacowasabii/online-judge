def solution(n):
    ans = 0
    arr = [True] * (n + 1)
    for i in range(2, n + 1):
        for j in range(2, n // i + 1):
            arr[i * j] = False
    for i in arr[2:]:
        if i:
            ans += 1

    return ans