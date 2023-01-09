def solution(quiz):
    answer = []
    for q in quiz:
        p, a = q.split("=")
        if eval(p) == int(a):
            answer.append("O")
        else:
            answer.append("X")
    return answer
