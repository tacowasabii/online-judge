def solution(numbers, target):
    answer = [0]
    
    def cal(numbers, num, target):
        copy_numbers = list(numbers)
        n = copy_numbers.pop()
        if not copy_numbers:
            if target == num + n:
                answer[0] += 1
            if target == num - n:
                answer[0] += 1
        else:
            cal(copy_numbers, num + n, target)
            cal(copy_numbers, num - n, target)
    cal(numbers, 0, target)
    return answer[0]