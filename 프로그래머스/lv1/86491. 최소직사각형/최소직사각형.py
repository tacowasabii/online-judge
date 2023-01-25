def solution(sizes):
    row = 0
    col = 0
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
    for i in sizes:
        row = max(row, i[0])
        col = max(col, i[1])
    return row * col