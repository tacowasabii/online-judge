def solution(dots):
    answer = []
    for i in range(3):
        for j in range(1,4-i):
            answer.append((dots[i][0]-dots[i+j][0])/(dots[i][1]-dots[i+j][1]))
    return 0 if len(set(answer)) == len(answer) else 1