def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b').zfill(n)
        arr2[i] = format(arr2[i], 'b').zfill(n)

    for i in range(n):
        temp = []
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                temp.append(' ')
            else:
                temp.append('#')
        answer.append(''.join(temp))
    return answer