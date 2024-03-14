def solution(prices):
    answer = []
    dic = {}
    stack = []
    for i, v in enumerate(prices):
        while len(stack) > 0:
            tmp = stack.pop()
            if tmp[1] > v:
                dic[tmp[0]] = i - tmp[0]
            else:
                stack.append(tmp)
                break
        stack.append((i,v))
    if len(stack) > 0:
        for i in stack:
            dic[i[0]] = len(prices) - 1 - i[0]
            
    for i in range(len(prices)):
        answer += [dic[i]]
    return answer