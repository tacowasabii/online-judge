def compress(arr, x, y, n):
    init = arr[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != init:
                return compress(arr, x, y, n//2) + compress(arr, x + n//2, y, n//2) + compress(arr, x, y + n//2, n//2) + compress(arr, x + n//2, y + n//2, n//2)
    
    return [1] if init == 1 else [0]

def solution(arr):
    result = compress(arr, 0, 0, len(arr))
    return [result.count(0), result.count(1)]