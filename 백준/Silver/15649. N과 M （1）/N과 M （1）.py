def backtrack(selected, n, m):
    # 선택한 수열의 길이가 M이면 출력
    if len(selected) == m:
        print(" ".join(map(str, selected)))
        return

    # 가능한 모든 선택지에 대해 재귀 호출
    for i in range(1, n+1):
        if i not in selected:
            selected.append(i)
            backtrack(selected, n, m)
            selected.pop()

n, m = map(int, input().split())
backtrack([], n, m)