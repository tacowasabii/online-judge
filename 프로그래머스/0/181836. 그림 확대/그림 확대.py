def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        tmp = ''
        for j in picture[i]:
            tmp += j*k
        for l in range(k):
            answer.append(tmp)
    return answer