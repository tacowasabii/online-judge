def solution(k, score):
    answer = []
    stack = []
    for i in score:
        stack.append(i)
        if len(stack) < k:
            answer.append(sorted(stack,reverse=True)[-1])
        else:
            answer.append(sorted(stack,reverse=True)[k-1])
    return answer