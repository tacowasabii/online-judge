def solution(k, score):
    answer = []
    stack = []
    for i in range(min(k, len(score))):
        stack.append(score[i])
        stack.sort()
        answer.append(stack[0])
    for i in range(k, len(score)):
        stack.append(score[i])
        stack.sort()
        answer.append(stack[-k])
    return answer