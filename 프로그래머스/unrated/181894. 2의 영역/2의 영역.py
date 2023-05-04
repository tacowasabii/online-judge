def solution(arr):
    if 2 not in arr:
        return [-1]
    a = arr.index(2)
    tmp = arr[::-1]
    b = tmp.index(2)
    return arr[a:len(arr) - b]