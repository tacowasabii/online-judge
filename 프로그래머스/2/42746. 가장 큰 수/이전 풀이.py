def solution(numbers):
    answer = ''
    a = {}
    for i, n in enumerate(numbers):
        if len(str(n)) == 1:
            n *= 1111
        elif len(str(n)) == 2:
            n *= 101
        elif len(str(n)) == 3:
            n = n * 10 + n // 100
        a[i] = n

    sorted_dict = sorted(a.items(), key=lambda item: item[1], reverse=True)

    for i in sorted_dict:
        answer += str(numbers[i[0]])
        
    if set(numbers)=={0}:
        answer='0'

    return answer