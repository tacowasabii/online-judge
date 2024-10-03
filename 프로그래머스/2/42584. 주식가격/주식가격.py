def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, v in enumerate(prices):
        while stack and prices[stack[-1]] > v:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    for i in stack:
        answer[i] = len(prices) - i - 1
    return answer