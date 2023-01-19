def solution(score):
    answer = []
    for i in range(len(score)):
        score[i] = (score[i][0] + score[i][1]) / 2
    temp = sorted(score,reverse=True)
    for i in score:
        answer.append(temp.index(i)+1)
    return answer
