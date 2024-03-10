def solution(arr):
    answer = 0
    while True:
        tmp = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                tmp.append(i // 2)
            elif i < 50 and i % 2 != 0:
                tmp.append(i * 2 + 1)
            else:
                tmp.append(i)
        if tmp == arr:
            return answer
        else:
            arr = tmp
        answer += 1
    return answer