def solution(selected, n, m):
    if len(selected) == (m + 1):
        print(" ".join(map(str, selected[1:])))
        return

    for i in range(1, n + 1):
        if i > selected[-1]:
            selected.append(i)
            solution(selected, n, m)
            selected.pop()


n, m = map(int, input().split())
solution([0], n, m)