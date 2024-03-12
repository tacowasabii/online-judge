def solution(cacheSize, cities):
    answer = 0
    stack = []
    for i in cities:
        if i.lower() not in stack:
            stack.append(i.lower())
            answer += 5
            if len(stack) > cacheSize:
                stack.pop(0)
        else:
            stack.remove(i.lower())
            stack.append(i.lower())
            answer += 1
    return answer