def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for i in range(row):
            for j in range(row-col):
                arr[i].append(0)
    elif row < col:
        tmp = [0 for i in range(col)]
        for j in range(col-row):
            arr.append(tmp)
    return arr