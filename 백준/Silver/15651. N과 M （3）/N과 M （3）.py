def solution(selected, n, m):
    if len(selected) == m:
        print(" ".join(map(str, selected)))
        return

    for i in range(1, n + 1):
        selected.append(i)
        solution(selected, n, m)
        selected.pop()


n, m = map(int, input().split())
solution([], n, m)