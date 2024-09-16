def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        a1 = bin(arr1[i])[2:].zfill(n)
        a2 = bin(arr2[i])[2:].zfill(n)
        tmp = ""
        for i in range(n):
            if a1[i] == '1' or a2[i] == '1':
                tmp += "#"
            else:
                tmp += " "
        result.append(tmp)
    return result