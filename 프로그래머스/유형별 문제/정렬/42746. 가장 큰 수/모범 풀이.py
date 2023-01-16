def solution(numbers):
    numbers = [str(x) for x in numbers]  # O(n)
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)  # O(nlogn)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)  # O(n)
    return answer

# O(nlogn)