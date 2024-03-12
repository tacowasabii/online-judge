def solution(numbers, target):
    answer = [0]
    def sol(numbers, target, value, idx):
        if len(numbers) == idx:
            if target == value:
                answer[0] += 1
        else:
            a = numbers[idx]
            sol(numbers, target, value - a, idx + 1)
            sol(numbers, target, value + a, idx + 1)
    sol(numbers, target, 0, 0)
    return answer[0]