def solution(arr):
    count = 0
    if len(arr) == 1:
        return arr
    while True:
        if 2**count < len(arr) <= 2**(count+1):
            for i in range(2**(count+1) - len(arr)):
                arr.append(0)
            return arr
        count += 1