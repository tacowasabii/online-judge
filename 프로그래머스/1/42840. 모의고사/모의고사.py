def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    ss = [s1,s2,s3]
    
    scores = []
    for i in ss:
        score = 0
        for idx, v in enumerate(answers):
            if v == i[idx % len(i)]:
                score += 1
        scores.append(score)
        
    for i, v in enumerate(scores):
        if v == max(scores):
            answer.append(i+1)
    return answer